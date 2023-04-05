from django.urls import path
from api.chat.views import ChatView, index, room

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    # path("index/", index, name="index"),
    # path("index/<str:room_name>/", room, name="room"),
]
