import logging

from .base import *

INSTALLED_APPS += ['django_extensions', 'nplusone.ext.django']

MIDDLEWARE.insert(0, 'nplusone.ext.django.NPlusOneMiddleware',)

NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN
