from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import SchoolUser, EmployerUser
from .serializers import SchoolUserSerializer, EmployerUserSerializer


class SchoolUserApi(ListCreateAPIView):
    serializer_class = SchoolUserSerializer
    permission_classes = [IsAuthenticated]

    def get_user_id(self) -> int:
        user_id = Token.objects.get(key=self.request.auth.key).user_id
        return user_id

    def get_queryset(self):
        return SchoolUser.objects.filter(user_id=self.get_user_id())

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'user_id': self.get_user_id()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        SchoolUser.objects.create(**data);
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EmployerUserApi(ListCreateAPIView):
    serializer_class = EmployerUserSerializer
    permission_classes = [IsAuthenticated]

    def get_user_id(self) -> int:
        user_id = Token.objects.get(key=self.request.auth.key).user_id
        return user_id

    def get_queryset(self):
        return EmployerUser.objects.filter(user_id=self.get_user_id())

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'user_id': self.get_user_id()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        EmployerUser.objects.create(**data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
