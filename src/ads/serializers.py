from rest_framework.serializers import ModelSerializer

from .models import AdPhoto, Ad, AdSchedule, AdCategory


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'title', 'description', 'owner', 'payment', 'category', 'address', 'users')


class AdPhotoSerializer(ModelSerializer):
    class Meta:
        model = AdPhoto
        fields = ('id', 'photo', 'ad')


class AdCategorySerializer(ModelSerializer):
    class Meta:
        model = AdCategory
        fields = ('id', 'name')


class AdScheduleSerializer(ModelSerializer):
    class Meta:
        model = AdSchedule
        fields = ('id', 'start', 'stop', 'week_day', 'ad')