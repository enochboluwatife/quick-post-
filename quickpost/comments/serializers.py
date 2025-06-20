from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ('author',)

    def create(self, validated_data):
        # Ensure the author is the authenticated user
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
