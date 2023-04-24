from rest_framework import generics, filters, permissions
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import DogProfile
from .serializers import DogProfileSerializer
# from .serializers import DogProfileDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


# class DogProfileList(generics.ListAPIView):
class DogProfileList(generics.ListCreateAPIView):

    # def get(self, request):
    #     queryset = DogProfile.objects.annotate(
    #         posts_count=Count('owner__post', distinct=True),
    #         followers_count=Count('owner__followed', distinct=True),
    #         following_count=Count('owner__following', distinct=True)
    #     ).order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DogProfileSerializer
    queryset = DogProfile.objects.all().order_by('-created_at')
# serializer_class = DogProfileSerializer(dogprofiles, many = 'True')
    filter_backends = [
        filters.OrderingFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
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


class DogProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DogProfileSerializer
    # queryset = DogProfile.objects.all()
    queryset = DogProfile.objects.annotate().order_by('-created_at')
