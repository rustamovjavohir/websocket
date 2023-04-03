from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ChatView(TemplateView):
    template_name = 'chat/lobby.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
