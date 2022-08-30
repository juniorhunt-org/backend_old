from rest_framework.routers import DefaultRouter

from .views import AdList, AdCategoryList, AdPhotoList, AdScheduleList, AdUserApi

router = DefaultRouter()
router.register('ad', AdList, 'ad_base')
router.register('photo', AdPhotoList, 'ad_photo')
router.register('category', AdCategoryList, 'ad_category')
router.register('schedule', AdScheduleList, 'ad_schedule')
router.register('add_user', AdUserApi, 'add_user')

urlpatterns = router.urls
