from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child("static")]

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child("media")
