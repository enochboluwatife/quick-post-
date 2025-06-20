# users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Create the router and register the viewset for users
router = DefaultRouter()
router.register(r'', UserViewSet)  # Don't need to add 'users' again since it's already added in main urls.py

urlpatterns = [
    path('', include(router.urls)),  # Register the routes automatically with the router
]
