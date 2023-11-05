from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user.renderers import UserRenderer
from user.utils import get_tokens_for_user
from user.serializers import  UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserLogoutSerializer
from django.contrib.auth import get_user_model,authenticate
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'data':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'data':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
    
class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class UserLogoutView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserLogoutSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({'msg':'Logout Success'}, status=status.HTTP_200_OK)

class TokenRefreshView(APIView):
  #generate new access token from refresh token from TokenRefreshView class on simplejwt

  def post(self, request, format=None):
    pass