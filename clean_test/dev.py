from .settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'caduri',
        'USER': 'caduri',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': ''
    }
}
