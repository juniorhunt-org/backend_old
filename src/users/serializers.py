from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import User
from .models import UserAvatar

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserAvatarSerializer(ModelSerializer):
    class Meta:
        model = UserAvatar
        fields = '__all__'
