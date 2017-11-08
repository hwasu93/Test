# -*- coding: utf-8 -*-

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'riuk=ne^9gyo8+3k2p=0$w!4g#)@l_(v0$48##i^sr#xj3rym^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}