from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chat.models import Room, Message
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.message.models import Messages, TextMessage


# Create your views here.

class ChatView(TemplateView):
    template_name = 'chat/lobby.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


def index(request):
    return render(request, "chat/chat2.html")


def room(request, room_name):
    return render(request, "chat/chat2.html", {"room_name": room_name})


class ChatJsonView(TemplateView):
    template_name = 'chat/chat2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class ChatP2PView(TemplateView):
    template_name = 'chat/chatp2p.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class RoomListView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/rooms.html'
    login_url = '/admin/login/'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'rooms': Room.objects.all()
        })
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class RoomDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/room-detail.html'
    login_url = '/admin/login/'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_name = kwargs.get('room_name')
        context.update({
            'room': Room.objects.filter(name=room_name).first()
        })
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class MessageSendAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "general", {"type": "send_info_to_user_group",
                        "text": {"status": "done"}}
        )

        return Response({"status": True}, status=status.HTTP_200_OK)

    def post(self, request):
        msg = TextMessage.objects.create(owner=request.user, context={"message": request.data["message"]})
        socket_message = f"Message with id {msg.id} was created!"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"{request.user.id}-message", {"type": "send_last_message",
                                           "text": socket_message}
        )

        return Response({"status": True}, status=status.HTTP_201_CREATED)
