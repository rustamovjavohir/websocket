from django.contrib import admin
from apps.chat.models import Room, Message, Group


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_online_count')
    search_fields = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'content', 'timestamp')
    search_fields = ('user__username', 'room__name', 'content')
    list_filter = ('room',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'owner', 'type', 'created_at', 'updated_at']
    list_filter = ['owner', 'type', 'created_at', 'updated_at']
    search_fields = ['owner', 'type']
    readonly_fields = ['created_at', 'updated_at']
