from django.urls import path, re_path
from api.chat.views import ChatView, ChatP2PView, index, room

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('P2P/<str:room_name>/', ChatP2PView.as_view(), name='chatp2p'),
    # re_path(r'^P2P/?<room_name>/$', ChatP2PView.as_view(), name='chatp2p'),
    # path("index/", index, name="index"),
    # path("index/<str:room_name>/", room, name="room"),

]
