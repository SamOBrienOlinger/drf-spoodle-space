from django.contrib.auth import get_user_model
from django.test import override_settings
from rest_framework.test import APIClient, APITestCase


@override_settings(
    DEFAULT_FILE_STORAGE='django.core.files.storage.FileSystemStorage',
    JWT_AUTH_SECURE=False,
)
class JWTCookieAuthenticationTests(APITestCase):
    def setUp(self):
        self.username = 'auth-test-user'
        self.password = 'auth-test-password'
        get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
        )

    def login(self):
        return self.client.post(
            '/dj-rest-auth/login/',
            {'username': self.username, 'password': self.password},
            format='json',
        )

    def test_login_sets_access_and_refresh_cookies(self):
        response = self.login()

        self.assertEqual(response.status_code, 200)
        self.assertIn('my-app-auth', response.cookies)
        self.assertIn('my-refresh-token', response.cookies)

    def test_login_is_not_blocked_by_session_csrf_authentication(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username=self.username, password=self.password)

        response = client.post(
            '/dj-rest-auth/login/',
            {'username': self.username, 'password': self.password},
            format='json',
        )

        self.assertEqual(response.status_code, 200)

    def test_user_endpoint_accepts_access_cookie(self):
        login_response = self.login()
        client = APIClient()
        client.cookies['my-app-auth'] = login_response.cookies[
            'my-app-auth'
        ].value

        response = client.get('/dj-rest-auth/user/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], self.username)

    def test_invalid_access_cookie_returns_401_for_refresh_interceptor(self):
        client = APIClient()
        client.cookies['my-app-auth'] = 'invalid-or-expired-token'

        response = client.get('/dj-rest-auth/user/')

        self.assertEqual(response.status_code, 401)

    def test_refresh_cookie_issues_a_new_access_cookie(self):
        login_response = self.login()
        client = APIClient()
        client.cookies['my-refresh-token'] = login_response.cookies[
            'my-refresh-token'
        ].value

        response = client.post('/dj-rest-auth/token/refresh/', {}, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('my-app-auth', response.cookies)

    def test_user_endpoint_succeeds_after_cookie_refresh(self):
        login_response = self.login()
        client = APIClient()
        client.cookies['my-refresh-token'] = login_response.cookies[
            'my-refresh-token'
        ].value
        refresh_response = client.post(
            '/dj-rest-auth/token/refresh/', {}, format='json'
        )
        client.cookies['my-app-auth'] = refresh_response.cookies[
            'my-app-auth'
        ].value

        response = client.get('/dj-rest-auth/user/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], self.username)
