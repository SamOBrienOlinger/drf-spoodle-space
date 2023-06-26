from django.shortcuts import render
from rest_framework import generics, permissions, filters
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import DogDanger
from dogdanger.serializers import DogDangerSerializer, DogDangerDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DogDangerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DogDangerSerializer
    queryset = DogDanger.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'owner__username',
        'dangerously_cute',
    ]
    ordering_fields = [
        '-created_at'
    ]

    def perform_create(self, serializer):
        print("running?")
        serializer.save(owner=self.request.user)


class DogDangerDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DogDangerDetailSerializer
    queryset = DogDanger.objects.all().order_by('-created_at')
