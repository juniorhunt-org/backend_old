from .views import AdList, AdCategoryList, AdPhotoList, AdScheduleList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ad', AdList, 'ad_base')
router.register('photo', AdPhotoList, 'ad_photo')
router.register('category', AdCategoryList, 'ad_category')
router.register('schedule', AdScheduleList, 'ad_schedule')

urlpatterns = router.urls
