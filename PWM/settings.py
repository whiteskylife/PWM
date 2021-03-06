# -*- coding: utf-8 -*-
"""
Django settings for PWM project.

Generated by 'django-admin startproject' using Django 1.11.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y0@^myyuid!x4tmzwf-!0j4f8^)*a88%kl-#0c^v&@jhn*sm-='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'kombu.transport.django',
    # 'django_filters',
    'corsheaders',
    'mgmt',
    'monitor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'mgmt.csrf.DisableCSRF',
    # 'mgmt.csrf.DisableCSRF',
]

MIDDLEWARE_CLASSES = ('mgmt.csrf.DisableCSRF')

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = (
#    '*'
#)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

ROOT_URLCONF = 'PWM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

APPEND_SLASH=False

WSGI_APPLICATION = 'PWM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db7.sqlite3'),
    }
    # 'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'novel',
    #    'USER': 'novel',
    #    'PASSWORD': 'novel',
    #    'HOST': '10.50.182.29',
    #    'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# REST_FRAMEWORK = {
#     # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
#     "DEFAULT_AUTHENTICATION_CLASSES":["mgmt.utils.auth.Authtication",]
# }
DEFAULT_PARSER_CLASSES = (
    'rest_framework.parsers.JSONParser',
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.MultiPartParser',
),

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL = "/media/"

AUTH_USER_MODEL = "mgmt.UserInfo"
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'VERSION_PARAM': "version",
    'DEFAULT_VERSION': 'V1',
    'ALLOWED_VERSIONS': ['v1', 'v2']
}


RESTFUL_API = 'http://127.0.0.1:888/api/v1/'

REDIS_IP = '10.50.181.6'
REDIS_PORT = 6380

CONSUL_IP = '10.50.182.65'
CONSUL_PORT = 8500
CONSUL_JOB_DIR = 'prometheus-job'
CONSUL_PROMETHEUS_RULES_DIR = 'prometheus-rules'
CONSUL_ALERTMANAGER_DIR = 'alertmanager-config'

SMS_URL = 'http://172.18.100.168:20019/esbsmstrue/api/sms/general/send'
SENDMAIL_SMTP = 'smtp.jieyuechina.com:25'
SENDMAIL_SENDER = 'chaoyan1@jieyuechina.com'
SENDMAIL_SENDER_PASSWORD = 'Chinayc19880510#'

MONTIOR_REDIS = '10.50.182.65'
MONTIOR_PORT = 6379

WX_URL = 'http://outrel.jieyue.com/outrel/api/externalplatform/interfaceRest/extInterface/v2'

ALERTMANAGER_HTTP = 'http://10.50.182.65:9093'
ALERTMANAGER_SILENCES_URI = '/api/v2/silences'
ALERTMANAGER_SILENCES_DELETE_URI = '/api/v2/silence'
