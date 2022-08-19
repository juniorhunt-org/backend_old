from django.urls import path
from .views import SchoolUserApi, EmployerUserApi

urlpatterns = [
    path('school_user/', SchoolUserApi.as_view()),
    path('employer_user/', EmployerUserApi.as_view())
]
