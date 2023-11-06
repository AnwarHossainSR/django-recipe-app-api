from rest_framework.response import Response
from rest_framework import status, generics


class RecipeView(generics.CreateAPIView):

    def post(self, request, format=None):

        return Response({'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
