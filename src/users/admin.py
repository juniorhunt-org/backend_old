from django.contrib import admin

from .models import ProfileUser


@admin.register(ProfileUser)
class ProfileUsersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'second_name', 'address', 'gender', 'avatar', 'description', 'company_name',
        'avatar', 'is_company')
    search_fields = ('first_name', 'last_name', 'second_name', 'description', 'address')
