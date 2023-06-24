from rest_framework import generics, permissions
from spoodle_space.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    """ List all followers. Create a follow if authenticated. The perform_create method associates the follow with the logged in user. """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """ Retrieve a like. No Update view, as Userscan only like or unlike a post. Destroy a like, i.e. unlike a post if owner of that like """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
