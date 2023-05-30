from django.shortcuts import render
from rest_framework import generics, permissions, filters
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import DogHealth
from doghealth.serializers import DogHealthSerializer, DogHealthDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DogHealthList(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DogHealthSerializer
    queryset = DogHealth.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
         '-created_at'
    ]


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class DogHealthDetail(generics.RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DogHealthDetailSerializer
    queryset = DogHealth.objects.all()
