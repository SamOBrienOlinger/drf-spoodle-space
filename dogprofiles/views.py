from rest_framework import generics, filters, permissions
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import DogProfile
from .serializers import DogProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DogProfileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DogProfileSerializer
    queryset = DogProfile.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile'
    ]
    search_fields = [
        'owner__username',
        'dog_name',
    ]
    ordering_fields = [
        '-created_at'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DogProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DogProfileSerializer
    queryset = DogProfile.objects.all().order_by('-created_at')
