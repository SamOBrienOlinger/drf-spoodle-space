from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post

# Create your tests here.


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')
