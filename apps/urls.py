from django.urls import path, include

from apps.auth_user.urls import urlpatterns as auth_user_urls
from apps.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('', include(auth_user_urls)),
]
