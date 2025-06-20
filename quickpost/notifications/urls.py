# notifications/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet

router = DefaultRouter()
router.register(r'', NotificationViewSet)  # <-- Register with empty string!

urlpatterns = [
    path('', include(router.urls)),   # <-- no 'api/', just directly include
]
