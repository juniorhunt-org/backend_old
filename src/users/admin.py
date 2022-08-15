from django.contrib import admin

from .models import User


# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'first_name', 'last_name', 'second_name', 'email', 'phone', 'address')
    list_display_links = ('id',)
    search_fields = ('first_name', 'last_name', 'second_name', 'email', 'phone')
