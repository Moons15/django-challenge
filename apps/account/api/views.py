from rest_framework import generics, status
from rest_framework.response import Response
from apps.account.api.serializers import LoginSerializer, \
    CreateSuperUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        token, created = Token.objects.get_or_create(
            user=serializer.get_user())
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class CreateSuperUserAPIView(generics.CreateAPIView):
    serializer_class = CreateSuperUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
