from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import strings
from services.auth_user import UserService


class RegistrationPageView(TemplateView):
    template_name = 'colorlib-regform-7/index.html'
    user_service = UserService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "login"
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get("signin"):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if not user:
                return render(request, self.template_name, {"login_error": strings.LOGIN_OR_PASSWORD_INCORRECT})
            login(request, user)
            return redirect('home')
        elif request.POST.get("signup"):
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("pass")
            re_pass = request.POST.get("re_pass")

            context = {
                "type": "register",
            }

            if password != re_pass:
                context.update({"password_error": strings.PASSWORDS_NOT_MATCH})
                return render(request, self.template_name, context)
            if self.user_service.get_by_username(username):
                context.update({"username_error": strings.USERNAME_ALREADY_EXISTS})
                return render(request, self.template_name, context)

            user = self.user_service.create_user(username, email, password)
            login(request, user)
            return redirect('home')
