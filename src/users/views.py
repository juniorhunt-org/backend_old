from rest_framework.viewsets import ModelViewSet

from .models import User, UserAvatar

from .serializers import UserAvatarSerializer, UserSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserAvatarViewSet(ModelViewSet):
    serializer_class = UserAvatarSerializer
    queryset = UserAvatar.objects.all()
