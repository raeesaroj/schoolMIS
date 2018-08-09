"""
WSGI config for schoolmis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schoolmis.settings")
from django.conf import settings
if not settings.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schoolmis.settings.production") #for production
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schoolmis.settings.development") # for development

application = get_wsgi_application()
