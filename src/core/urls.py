from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/v1/', include('users.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/ads/', include('ads.urls'))
]
