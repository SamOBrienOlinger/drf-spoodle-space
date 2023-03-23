from rest_framework import generics, permissions
from Spoodle_Space.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowSerializer

# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    """ List all followers. Create a follow if authenticated. The perform_create method associates the follow with the logged in user. """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    """ Retrieve a like. No Update view, as users can only like or unlike a post. Destroy a like, i.e. unlike a post if owner of that like """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower().objects.all()
    serializer_class = FollowSerializer
