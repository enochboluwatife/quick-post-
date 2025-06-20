from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting comments.
    It supports filtering by post and author, sorting by created_at,
    and allows authenticated users to interact with the comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    # Enabling filtering by post and author, and sorting by created_at
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['post', 'author']  # Filter by post and author
    ordering_fields = ['created_at']  # Sort by creation date
    ordering = ['created_at']  # Default ordering by creation date (ascending)

    def perform_create(self, serializer):
        """
        Automatically set the author of the comment to the currently authenticated user.
        """
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def reply(self, request, pk=None):
        """
        Custom action for replying to a comment.
        Expects 'content' in the request data to create a reply.
        """
        parent_comment = self.get_object()  # Get the comment being replied to
        content = request.data.get('content')

        if content:
            # Create a new comment as a reply to the original comment
            reply = Comment.objects.create(
                post=parent_comment.post,  # Use the same post as the parent comment
                author=request.user,  # The current authenticated user is the author
                content=content,  # The content of the reply
                parent=parent_comment  # Set the parent to the original comment
            )
            serializer = CommentSerializer(reply)
            return Response(serializer.data, status=201)
        return Response({"detail": "Content is required to reply."}, status=400)
