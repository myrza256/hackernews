from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .models import Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsSelf


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or 'partial_update' or 'destroy':
            permission_classes = [IsSelf]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    @action(methods=['post'], detail=True)
    def upvote(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        check_user_voted = Post.objects.filter(id=pk, voted_by=request.user)
        if not check_user_voted:
            post.voted_by.add(request.user)
            post.amount_of_votes += 1
            post.save()
            return Response(status=status.HTTP_200_OK, data={'amount_of_votes': post.amount_of_votes})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "this user has already voted for this post"})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_pk = self.kwargs['post_pk']
        post = get_object_or_404(Post, id=post_pk)
        serializer.save(post=post, author=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or 'partial_update' or 'destroy':
            permission_classes = [IsSelf]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
