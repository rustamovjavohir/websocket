from django.shortcuts import render
from django.views.generic import TemplateView
from apps.chat.models import Room, Message


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


class RoomListView(TemplateView):
    template_name = 'chat/rooms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'rooms': Room.objects.all()
        })
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class RoomDetailView(TemplateView):
    template_name = 'chat/room-detail.html'

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
