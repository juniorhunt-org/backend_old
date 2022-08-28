from rest_framework.serializers import ModelSerializer

from .models import ProfileUser


class ProfileUserSerializer(ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = (
            'first_name', 'last_name', 'second_name', 'address', 'description', 'avatar', 'company_name', 'gender',
            'user_id',
            'contacts', 'is_company')
