from .base import *
import os

DEBUG = True

ROOT_URLCONF = 'configs.urls.development'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'