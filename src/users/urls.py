from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserAvatarViewSet, UserViewSet

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('avatar', UserAvatarViewSet)

urlpatterns = [
    path('', include(router.urls))
]
