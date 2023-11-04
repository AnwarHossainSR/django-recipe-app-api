from django.urls import path
from .views import UserProfileView, UserRegistrationView, UserLoginView


urlpatterns = [
        path('register', UserRegistrationView.as_view(), name='register'),
        path('login', UserLoginView.as_view(), name='login'),
        path('me', UserProfileView.as_view(), name='profile'),
]