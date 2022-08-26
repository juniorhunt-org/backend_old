from rest_framework.serializers import ModelSerializer
from .models import SchoolUser, EmployerUser


class SchoolUserSerializer(ModelSerializer):
    class Meta:
        model = SchoolUser
        fields = ('first_name', 'last_name', 'second_name', 'address', 'gender', 'avatar', 'description')


class EmployerUserSerializer(ModelSerializer):
    class Meta:
        model = EmployerUser
        fields = ('first_name', 'last_name', 'second_name', 'address', 'description', 'avatar', 'company_name')
