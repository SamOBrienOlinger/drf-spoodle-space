from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post

# Create your tests here.


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

# test 1

    def test_can_list_posts(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

# test 2

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# challenge test: We’ll test that when a user attempts to send a post request to ‘/posts’ to create a post, the response status code is 403, which stands for ‘FORBIDDEN’

    def test_logged_in_user_can_send_post(self):
        # self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        # count = Post.objects.count()
        # self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
