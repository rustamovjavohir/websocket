"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from api.chat.routing import websocket_urlpatterns
from config.middleware import WebSocketJWTAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # 'websocket': AuthMiddlewareStack(  # TODO BasicAuthMiddleware
    #     URLRouter(
    #         websocket_urlpatterns
    #     )
    # )
    'websocket': WebSocketJWTAuthMiddleware(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
