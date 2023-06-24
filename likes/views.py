from rest_framework import generics, permissions
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import Like
from likes.serializers import LikeSerializer


# Create your views here.


class LikeList(generics.ListCreateAPIView):
    """ List all likes. Create a like if authenticated. The perform_create method associates the like with the logged in user. """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """ Retrieve a like. No Update view, as Userscan only like or unlike a post. Destroy a like, i.e. unlike a post if owner of that like """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
