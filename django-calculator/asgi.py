"""
ASGI config for calculator_project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter  # Optional for WebSockets

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculator_project.settings')

# Base Django ASGI application
django_application = get_asgi_application()

# Optional WebSocket support (uncomment when needed)
# from calculator_app.routing import websocket_urlpatterns  # Create this later if needed
# from channels.auth import AuthMiddlewareStack
# from channels.routing import URLRouter

application = ProtocolTypeRouter({
    "http": django_application,
    # Uncomment when adding WebSocket support:
    # "websocket": AuthMiddlewareStack(
    #     URLRouter(
    #         websocket_urlpatterns
    #     )
    # ),
})

# Production optimizations (uncomment when needed)
# try:
#     from whitenoise import WhiteNoise
#     application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'static'))
# except ImportError:
#     pass