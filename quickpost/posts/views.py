from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated  # Add permission to ensure only authenticated users can create posts

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create or edit posts

    def perform_create(self, serializer):
        # Automatically set the author to the current user when creating a post
        serializer.save(author=self.request.user)
