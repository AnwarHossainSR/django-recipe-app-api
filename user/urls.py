from django.urls import path
from .views import CustomTokenRefreshView, TokenRefreshView, UserLogoutView, UserProfileView, UserRegistrationView, UserLoginView


urlpatterns = [
        path('register', UserRegistrationView.as_view(), name='register'),
        path('login', UserLoginView.as_view(), name='login'),
        path('token/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
        path('me', UserProfileView.as_view(), name='profile'),
        path('logout', UserLogoutView.as_view(), name='logout'),
]