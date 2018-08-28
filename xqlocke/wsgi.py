"""
WSGI config for xqlocke project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xqlocke.settings')
application = get_wsgi_application()
