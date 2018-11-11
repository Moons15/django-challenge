from .base import *

ALLOWED_HOSTS = ['178.128.9.218']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'challengedb',
        'USER': 'postgres',
        'PASSWORD': '992424558',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
APPSECRET_PROOF = False
