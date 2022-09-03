from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ProfileUser
from .permissions import IsOwnerOrReadOnly
from .serializers import ProfileUserSerializer


class ProfileUserApi(ModelViewSet):
    serializer_class = ProfileUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_user_id(self) -> int:
        user_id = Token.objects.get(key=self.request.auth.key).user_id
        return user_id

    def get_queryset(self):
        queryset = ProfileUser.objects.all()
        print(self.request.auth)
        if self.request.query_params.get('me') and self.request.auth is not None:
            return queryset.filter(user_id=self.get_user_id())
        else:
            return queryset

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'user_id': self.get_user_id()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        ProfileUser.objects.create(**data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
