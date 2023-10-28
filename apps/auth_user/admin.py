from django.contrib import admin
from apps.auth_user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_active', 'is_online')
    list_filter = ('is_staff', 'is_active', 'is_online')
    search_fields = ('username',)
