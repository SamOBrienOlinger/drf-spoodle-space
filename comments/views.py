from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer
from Spoodle_Space.permissions import IsOwnerOrReadOnly

# Create your views here.


# class CommentDetailSerializer(CommentSerializer):
class CommentList(APIView):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(
            comments, many=True, context={'request': request}
        )
        return Response(serializer.data)


class CommentDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(
            comment, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = PostSerializer(
            comment, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
