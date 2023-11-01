from django.contrib import admin
from apps.message.models import TextMessage


@admin.register(TextMessage)
class TextMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'group', 'reply', 'created_at', 'updated_at']
    list_filter = ['owner', 'group', 'reply', 'created_at', 'updated_at']
    search_fields = ['owner', 'group']
    readonly_fields = ['created_at', 'updated_at']
