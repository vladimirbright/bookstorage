# -*- coding: utf-8 -*-

import os.path

SELF_DIR = os.path.abspath(os.path.dirname(__file__))

def self_dir(name=''):
    return os.path.join(SELF_DIR, name)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vladimir', 'vladimirbright@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = self_dir('s')
MEDIA_URL = '/s/'
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gs8l_)51oyyla)$3@bt@*o%vnm&&yihz$7j&$trm#&vku96*k4'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    self_dir('templates'),
)

INSTALLED_APPS = (
    'authors',
    'books',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'south',
    'easy_thumbnails',
)


try:
    from local_settings import *
except ImportError:
    pass

