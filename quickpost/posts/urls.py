# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'', PostViewSet)  # Register with an empty string to allow /api/posts/

urlpatterns = [
    path('', include(router.urls)),
]
