"""
WSGI config for calculator_project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'wsgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculator_project.settings')

# Create the WSGI application object
application = get_wsgi_application()

# Optional: Add middleware for production (example with WhiteNoise)
try:
    from whitenoise import WhiteNoise
    application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'static'))
    # Enable compression
    application.add_files(os.path.join(os.path.dirname(__file__), 'static'), prefix='static/')
except ImportError:
    pass  # WhiteNoise not installed