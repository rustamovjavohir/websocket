from django.urls import path
from api.chat.views import ChatView

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
]
