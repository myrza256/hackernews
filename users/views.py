from operator import ge
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken

from users.models import User
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.save()
            _, token = AuthToken.objects.create(user)
            user = UserSerializer(
                user, context=self.get_serializer_context()).data
            response = {
                'response': True,
                'token': token,
                'user': user
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            errors = serializer.errors
            x = next(iter(errors))
            error = errors[x][0]
            data = {'response': False,
                    'error_message': error, }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.validated_data
            _, token = AuthToken.objects.create(user)
            user = UserSerializer(
                user, context=self.get_serializer_context()).data
            response = {
                'response': True,
                'token': token,
                'user': user
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            data = {'response': False,
                    'error_message': 'Invalid login or password'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

