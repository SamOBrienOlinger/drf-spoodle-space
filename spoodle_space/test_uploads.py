import io
from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from posts.models import Post
from dogprofiles.models import DogProfile
from doghealth.models import DogHealth
from dogdanger.models import DogDanger
from profiles.models import Profile


def image_file(size=(20, 20), name='dog.png'):
    buffer = io.BytesIO()
    Image.new('RGB', size, (120, 80, 190)).save(buffer, format='PNG')
    return SimpleUploadedFile(name, buffer.getvalue(), content_type='image/png')


class CommunityUploadTests(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='example')
        self.other = User.objects.create_user(username='visitor', password='example')
        self.client.force_authenticate(self.owner)

    def test_text_only_post_and_remove_existing_photo(self):
        response = self.client.post('/posts/', {'title': 'A walk'}, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertFalse(response.data['image'])
        pk = response.data['id']
        uploaded = self.client.patch(f'/posts/{pk}/', {'image': image_file()}, format='multipart')
        self.assertEqual(uploaded.status_code, 200)
        self.assertTrue(uploaded.data['image'])
        removed = self.client.patch(f'/posts/{pk}/', {'image': ''}, format='multipart')
        self.assertEqual(removed.status_code, 200)
        self.assertFalse(removed.data['image'])
        self.assertFalse(Post.objects.get(pk=pk).image)

    def test_image_size_errors_are_identical_across_uploads(self):
        endpoints = [('/posts/', 'image', {'title': 'Large'}),
                     ('/dogprofiles/', 'dog_profile_image', {'dog_name': 'Riley'}),
                     (f'/profiles/{self.owner.profile.pk}/', 'image', {})]
        messages = []
        for url, field, data in endpoints:
            upload = SimpleUploadedFile('large.png', b'x' * (2 * 1024 * 1024 + 1), content_type='image/png')
            response = (self.client.patch if url.startswith('/profiles/') else self.client.post)(url, {**data, field: upload}, format='multipart')
            self.assertEqual(response.status_code, 400)
            self.assertIsInstance(response.data[field], list)
            messages.append(str(response.data[field][0]))
        self.assertEqual(len(set(messages)), 1)
        self.assertIn('2 MB', messages[0])

    def test_dimensions_boundary_and_invalid_file(self):
        for size in [(4097, 1), (1, 4097)]:
            response = self.client.post('/posts/', {'title': 'Too wide or tall', 'image': image_file(size)}, format='multipart')
            self.assertEqual(response.status_code, 400)
            self.assertIn('4096', str(response.data['image']))
        valid = self.client.post('/posts/', {'title': 'Boundary', 'image': image_file((4096, 1))}, format='multipart')
        self.assertEqual(valid.status_code, 201)
        invalid = self.client.post('/posts/', {'title': 'Invalid', 'image': SimpleUploadedFile('bad.jpg', b'not an image', content_type='image/jpeg')}, format='multipart')
        self.assertEqual(invalid.status_code, 400)
        self.assertIn('could not be read', str(invalid.data['image']))

    def test_duplicate_dog_records_return_actionable_validation(self):
        for model, endpoint in [(DogProfile, 'dogprofiles'), (DogHealth, 'doghealth'), (DogDanger, 'dogdanger')]:
            model.objects.create(owner=self.owner)
            response = self.client.post(f'/{endpoint}/', {}, format='json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('My dog', str(response.data['non_field_errors']))
            self.assertEqual(model.objects.filter(owner=self.owner).count(), 1)

    def test_profile_ids_do_not_depend_on_user_ids(self):
        profile_id = self.other.profile.pk + 50
        Profile.objects.filter(owner=self.owner).update(id=profile_id)
        dog = DogProfile.objects.create(owner=self.owner, dog_name='Riley')
        health = DogHealth.objects.create(owner=self.owner)
        behaviour = DogDanger.objects.create(owner=self.owner)
        response = self.client.get(f'/profiles/{profile_id}/')
        self.assertEqual(response.data['dog_profile'], dog.pk)
        self.assertEqual(response.data['dog_health'], health.pk)
        self.assertEqual(response.data['dog_danger'], behaviour.pk)
        for endpoint, record in [('dogprofiles', dog), ('doghealth', health), ('dogdanger', behaviour)]:
            self.assertEqual(self.client.get(f'/{endpoint}/{record.pk}/').data['profile_id'], profile_id)

    def test_permissions_not_found_and_validation_keep_json_errors(self):
        post = Post.objects.create(owner=self.other, title='Another member')
        denied = self.client.delete(f'/posts/{post.pk}/')
        self.assertEqual(denied.status_code, 403)
        self.assertIn('detail', denied.data)
        missing = self.client.get('/posts/99999/')
        self.assertEqual(missing.status_code, 404)
        self.assertIn('detail', missing.data)
        empty_comment = self.client.post('/comments/', {'post': post.pk, 'content': '  '}, format='json')
        self.assertEqual(empty_comment.status_code, 400)
        self.assertIn('content', empty_comment.data)
        email = self.client.post('/doghealth/', {'vet_email': 'invalid'}, format='json')
        self.assertEqual(email.status_code, 400)
        self.assertIn('vet_email', email.data)
        self.client.force_authenticate(user=None)
        anonymous = self.client.post('/posts/', {'title': 'Not signed in'}, format='json')
        self.assertIn(anonymous.status_code, [401, 403])
        self.assertIn('sign in', str(anonymous.data['detail']))
