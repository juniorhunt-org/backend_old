from rest_framework.routers import DefaultRouter

from .views import ProfileUserApi, NotificationTokenApi

router = DefaultRouter()
router.register('profile_user', ProfileUserApi, 'profile_user')
router.register('user_notification', NotificationTokenApi, 'notification_user')
urlpatterns = router.urls
