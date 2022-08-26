from django.contrib import admin

from .models import AdCategory, AdSchedule, Ad, AdPhoto


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'limit', 'payment', 'description', 'category')
    search_fields = ('title', 'payment', 'description')
    list_filter = ('category', 'limit', 'payment')


@admin.register(AdCategory)
class AdCategory(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(AdSchedule)
class AdScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'stop', 'week_day', 'ad')


@admin.register(AdPhoto)
class AdPhoto(admin.ModelAdmin):
    list_display = ('id', 'photo', 'ad')
