from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import UserAvatarViewSet, UserViewSet

router = SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'avatar', UserAvatarViewSet)


urlpatterns = [
    path('', include(router.urls))
]
