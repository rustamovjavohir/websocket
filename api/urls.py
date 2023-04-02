from django.urls import path, include

urlpatterns = [
    # path('auth-user/', include('api.auth_user.urls')),
    path('chat/', include('api.chat.urls')),
]
