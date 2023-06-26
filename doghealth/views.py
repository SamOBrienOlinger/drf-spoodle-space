from rest_framework import generics, permissions, filters
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import DogHealth
from doghealth.serializers import DogHealthSerializer
from doghealth.serializers import DogHealthDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DogHealthList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DogHealthSerializer
    queryset = DogHealth.objects.all()

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
        'vet_name'
    ]
    ordering_fields = [
        '-created_at'
    ]

    def perform_create(self, serializer):
        print("running?")
        serializer.save(owner=self.request.user)


class DogHealthDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DogHealthDetailSerializer
    serializer_class = DogHealthSerializer
    queryset = DogHealth.objects.all().order_by('-created_at')
