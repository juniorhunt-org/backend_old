from rest_framework.serializers import ModelSerializer

from .models import ProfileUser, UserNotification


class ProfileUserSerializer(ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('id',
                  'first_name', 'last_name', 'second_name', 'address', 'description', 'avatar', 'company_name',
                  'gender',
                  'user_id',
                  'contacts', 'is_company')


class UserNotificationSerializer(ModelSerializer):
    class Meta:
        model = UserNotification
        fields = ('id', 'user', 'user_id', 'token')
