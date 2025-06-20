from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        """
        Optionally restrict the returned users to a subset, by filtering
        against a 'username' query parameter in the URL.
        """
        queryset = CustomUser.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

    def perform_create(self, serializer):
        """
        Create a new user instance with additional logic if needed
        (like setting default fields or sending notifications).
        """
        # Add any custom logic for user creation, if required
        serializer.save()
