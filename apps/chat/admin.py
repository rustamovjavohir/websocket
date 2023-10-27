from django.contrib import admin
from apps.chat.models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_online_count')
    search_fields = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'content', 'timestamp')
    search_fields = ('user__username', 'room__name', 'content')
    list_filter = ('room',)
