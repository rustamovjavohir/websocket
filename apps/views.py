from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def error_404(request, exception):
    return render(request, '404.html', {})


def error_500(request, *args, **argv):
    return render(request, '500.html', status=500)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'chat1.html'
    login_url = '/auth/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
