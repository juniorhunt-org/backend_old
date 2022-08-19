from django.contrib import admin

from .models import SchoolUser, EmployerUser


@admin.register(SchoolUser)
class SchoolUsersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'second_name', 'address', 'gender', 'avatar', 'description')
    search_fields = ('first_name', 'last_name', 'second_name', 'description', 'address')


@admin.register(EmployerUser)
class EmployerUsersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'second_name', 'address', 'description', 'company_name', 'avatar')
    search_fields = ('first_name', 'last_name', 'second_name', 'description', 'address')
