from django.urls import re_path
from api.chat.consumers import ChatConsumer, ChatConsumer2, ChatP2PConsumer, ChatRoomConsumer, ApiChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', ChatConsumer.as_asgi()),
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer2.as_asgi()),
    re_path(r"ws/p2p/", ChatP2PConsumer.as_asgi()),
    re_path(r"ws/chat/rooms/(?P<room_name>\w+)/$", ChatRoomConsumer.as_asgi(), name="room"),
    re_path(r"ws/api/msg/", ApiChatConsumer.as_asgi(), name="api-msg"),
]
