from django.shortcuts import render

from django.db.models import Count
from rest_framework import generics, filters
from Spoodle_Space.permissions import IsOwnerOrReadOnly
from .models import DogProfile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class DogProfileList(generics.ListAPIView):
    queryset = DogProfile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = DogProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
        # 'likes__owner__profile',
        # 'owner__profile'
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = DogProfile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = DogProfileSerializer
