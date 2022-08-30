from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AdList, AdCategoryList, AdPhotoList, AdScheduleList, AdUserApi, AdReplyUserApi

router = DefaultRouter()
router.register('ad', AdList, 'ad_base')
router.register('photo', AdPhotoList, 'ad_photo')
router.register('category', AdCategoryList, 'ad_category')
router.register('schedule', AdScheduleList, 'ad_schedule')

urlpatterns = [*router.urls, path('reply_ads/', AdReplyUserApi.as_view()), path('add_user/', AdUserApi.as_view())]
