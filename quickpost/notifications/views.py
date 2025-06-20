from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and interacting with notifications.
    Notifications can be marked as read by the user.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    # Filter to show notifications only for the authenticated user
    def get_queryset(self):
        # Ensure you are using an authenticated user and that it's a valid CustomUser instance
        return Notification.objects.filter(recipient=self.request.user)

    # Mark notification as read
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        try:
            notification = self.get_object()
        except Notification.DoesNotExist:
            raise NotFound(detail="Notification not found")
        
        notification.mark_as_read()
        serializer = NotificationSerializer(notification)
        return Response({
            'status': 'notification marked as read',
            'notification': serializer.data
        })
