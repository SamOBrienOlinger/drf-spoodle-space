from django.shortcuts import render
from rest_framework import generics, permissions, filters
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import DogHealth
from dogdanger.serializers import DogDangerSerializer, DogDangerDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DogDangerList(generics.ListAPIView):
    #     queryset = DogHealth.objects.annotate(
    #     posts_count=Count('owner__post', distinct=True),
    #     followers_count=Count('owner__followed', distinct=True),
    #     following_count=Count('owner__following', distinct=True)
    # ).order_by('-created_at')
    # serializer_class = ProfileSerializer
    # filter_backends = [
    #     filters.OrderingFilter,
    #     DjangoFilterBackend,
    # ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DogDangerSerializer
    queryset = DogDanger.objects.all()

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
         '-created_at'
    ]

    # ordering_fields = [
    #     'posts_count',
    #     'followers_count',
    #     'following_count',
    #     'owner__following__created_at',
    #     'owner__followed__created_at',
    # ]


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class DogDangerDetail(generics.RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DogDangerDetailSerializer
    queryset = DogDangerDetail().objects.all()
