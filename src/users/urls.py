from django.urls import path
from .views import ProfileUserApi

urlpatterns = [
    path('profile_user/', ProfileUserApi.as_view())
]
