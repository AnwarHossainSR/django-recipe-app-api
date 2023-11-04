from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from user.utils import get_tokens_for_user
from user.serializers import  UserRegistrationSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationView(APIView):
  def post(self, request, format=None):
    print(request.data)
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'data':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
