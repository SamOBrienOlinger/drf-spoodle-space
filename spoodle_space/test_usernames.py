import string

from django.contrib.auth import get_user_model
from django.test import override_settings
from rest_framework.test import APIClient, APITestCase


@override_settings(
    DEFAULT_FILE_STORAGE='django.core.files.storage.FileSystemStorage',
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    JWT_AUTH_SECURE=False,
)
class FlexibleUsernameTests(APITestCase):
    password = 'Unrelated-secure-password#42!'

    def register(self, username):
        return APIClient().post(
            '/dj-rest-auth/registration/',
            {
                'username': username,
                'password1': self.password,
                'password2': self.password,
            },
            format='json',
        )

    def login(self, username, password=None, client=None):
        return (client or APIClient()).post(
            '/dj-rest-auth/login/',
            {'username': username, 'password': password or self.password},
            format='json',
        )

    def create_user(self, username):
        return get_user_model().objects.create_user(
            username=username, password=self.password,
        )

    def test_registration_and_cookie_login_accept_flexible_names(self):
        for username in (
            'Sam O’Brien-Olinger',
            'Sam & Benji #42!',
            '100% dog people 🐾',
            '1234567890',
            string.punctuation,
            '爱狗的人 123 🐶',
            'مُحِب الكلاب ١٢٣',
            'Dog family 👨‍👩‍👧‍👦',
            '<b>Benji & friends</b>',
        ):
            with self.subTest(username=username):
                response = self.register(username)
                self.assertEqual(response.status_code, 201, response.data)
                user = get_user_model().objects.get(username=username)
                self.assertEqual(user.username, username)

                response = self.login(username)
                self.assertEqual(response.status_code, 200, response.data)
                client = APIClient()
                client.cookies['my-app-auth'] = response.cookies[
                    'my-app-auth'
                ].value
                current_user = client.get('/dj-rest-auth/user/')
                self.assertEqual(current_user.status_code, 200)
                self.assertEqual(current_user.data['username'], username)
                self.assertEqual(current_user.data['profile_id'], user.profile.id)

    def test_outer_whitespace_is_trimmed_but_internal_spaces_are_kept(self):
        supplied = '  Sam  & Benji 🐾  '
        expected = 'Sam  & Benji 🐾'
        response = self.register(supplied)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertTrue(
            get_user_model().objects.filter(username=expected).exists()
        )
        response = self.login(supplied)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data['user']['username'], expected)

    def test_blank_and_overlong_registration_names_are_rejected(self):
        for username in ('', '   ', '\u2003', 'a' * 151, '🐾' * 151):
            with self.subTest(username=username):
                response = self.register(username)
                self.assertEqual(response.status_code, 400)
                self.assertIn('username', response.data)
        self.assertEqual(get_user_model().objects.count(), 0)

    def test_registration_accepts_150_characters_including_emoji(self):
        for username in ('a' * 150, '🐾' * 150):
            with self.subTest(username=username):
                response = self.register(username)
                self.assertEqual(response.status_code, 201, response.data)
                self.assertEqual(self.login(username).status_code, 200)

    def test_duplicate_names_remain_unavailable_regardless_of_case(self):
        self.create_user('Sam & Benji 🐾')
        for username in ('Sam & Benji 🐾', 'sam & benji 🐾'):
            with self.subTest(username=username):
                response = self.register(username)
                self.assertEqual(response.status_code, 400)
                self.assertIn('username', response.data)
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_changing_to_a_flexible_name_preserves_account_and_login(self):
        user = self.create_user('original-user')
        profile_id = user.profile.id
        self.assertEqual(
            self.login(user.username, client=self.client).status_code, 200
        )
        username = 'Benji / Sam & friends #7 🐾'
        response = self.client.put(
            '/dj-rest-auth/user/', {'username': username}, format='json',
        )
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data['username'], username)
        self.assertEqual(response.data['profile_id'], profile_id)
        user.refresh_from_db()
        self.assertEqual(user.username, username)
        self.assertEqual(self.login(username).status_code, 200)
        self.assertEqual(self.login('original-user').status_code, 400)

    def test_saving_an_unchanged_name_or_own_case_change_is_allowed(self):
        user = self.create_user('Sam & Benji 🐾')
        self.client.force_authenticate(user)
        for username in ('Sam & Benji 🐾', 'sam & benji 🐾'):
            with self.subTest(username=username):
                response = self.client.put(
                    '/dj-rest-auth/user/', {'username': username}, format='json',
                )
                self.assertEqual(response.status_code, 200, response.data)
                self.assertEqual(response.data['username'], username)

    def test_rename_rejects_another_accounts_name_including_case_variants(self):
        self.create_user('Sam & Benji 🐾')
        user = self.create_user('Another account!')
        self.client.force_authenticate(user)
        for username in ('Sam & Benji 🐾', 'sam & benji 🐾'):
            with self.subTest(username=username):
                response = self.client.put(
                    '/dj-rest-auth/user/', {'username': username}, format='json',
                )
                self.assertEqual(response.status_code, 400)
                self.assertIn('username', response.data)
        user.refresh_from_db()
        self.assertEqual(user.username, 'Another account!')

    def test_rename_retains_blank_and_length_validation(self):
        user = self.create_user('Original name!')
        self.client.force_authenticate(user)
        for username in ('', '   ', 'a' * 151, '🐾' * 151):
            with self.subTest(username=username):
                response = self.client.put(
                    '/dj-rest-auth/user/', {'username': username}, format='json',
                )
                self.assertEqual(response.status_code, 400)
                self.assertIn('username', response.data)
        user.refresh_from_db()
        self.assertEqual(user.username, 'Original name!')

    def test_flexible_username_still_requires_the_correct_password(self):
        username = 'Sam & Benji 🐾'
        self.create_user(username)
        response = self.login(username, password='Not-the-right-password!')
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('my-app-auth', response.cookies)
