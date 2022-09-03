from rest_framework.routers import DefaultRouter

from .views import ProfileUserApi

router = DefaultRouter()

router.register('profile_user', ProfileUserApi, 'profile_user')

urlpatterns = router.urls
