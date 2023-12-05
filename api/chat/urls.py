from django.urls import path, re_path
from api.chat.views import ChatView, ChatP2PView, index, room, RoomListView, RoomDetailView, MessageSendAPIView

urlpatterns = [
    # path('', ChatView.as_view(), name='chat'),
    path('p2p/<str:room_name>/', ChatP2PView.as_view(), name='chatp2p'),
    # re_path(r'^P2P/?<room_name>/$', ChatP2PView.as_view(), name='chatp2p'),
    # path("index/", index, name="index"),
    # path("index/<str:room_name>/", room, name="room"),
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('rooms/<str:room_name>/', RoomDetailView.as_view(), name='room-detail'),
    path('message/', MessageSendAPIView.as_view()),
]
