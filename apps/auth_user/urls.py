from django.urls import path

from apps.auth_user.views import RegistrationPageView

urlpatterns = [
    path('auth/', RegistrationPageView.as_view(), name='registration'),
]



