# coding: utf-8
"""
Django settings for hackthefutureclube project.
author: @alanwikid 2014
"""

import os
import sys
from decouple import config
from unipath import Path


BASE_DIR = Path(__file__).parent

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.herokuapp.com', '.hackthefuture.club']

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)),

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
)

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (os.path.join(BASE_DIR, 'templates'), ),
    },
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
