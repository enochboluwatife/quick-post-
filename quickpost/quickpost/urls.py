# quickpost/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Prefix the API routes properly, no need for additional 'api/' inside each app's urls.
    path('api/users/', include('users.urls')),  # Use '/api/users/' for user-related URLs
    path('api/posts/', include('posts.urls')),  # Use '/api/posts/' for post-related URLs
    path('api/comments/', include('comments.urls')),  # Use '/api/comments/' for comment-related URLs
    path('api/notifications/', include('notifications.urls')),  # Use '/api/notifications/' for notification-related URLs

    # JWT token routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
