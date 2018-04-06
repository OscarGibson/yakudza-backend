"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^w_dxe*)60j&uqkyn-b9!w**s@@dzcg286aa4041ol8(d41@n*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.yakuzalviv.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'rest_framework',
    'corsheaders',
    # 'django_facebook',
    # Custom apps
    'base',
    'category',
    'tag',
    'product',
    'order',
    'feedback',
    'section',
    'callback',
    'subscribers',
    'page',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'base.middleware.DisableCSRF,'
]

ROOT_URLCONF = 'src.urls'

# For "django_facebook" app
# this app user TEMPLATE_CONTEXT_PROCESSORS, 
# which is deprecated since django 1.8
TEMPLATE_CONTEXT_PROCESSORS = [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django_facebook.context_processors.facebook',
            ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]


WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Authentication backends

AUTHENTICATION_BACKENDS = (
    # 'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    'www.yakuzalviv.com'
)

# FACEBOOK fields

# FACEBOOK_APP_ID = '1534958043469587'
# FACEBOOK_APP_SECRET = 'bac9b64e9c09025535c6c411df3f5cab'
# FACEBOOK_ACCESS_TOKEN = 'EAACV48Uk99oBAGHF7tHqWH4ZBfA7hBUbQcOUgfdu598Ae3QOIoGP7hNnVwbXDdiaMKJogfPSXqaFHdvrh5oSJ1ZAFy6JSHByW5uoXtPZBGmABFsUHafqhW5jmgrBKQR9lH3Wk9KYMGqOkwcOS0ZBq34USVKZBKVZANOTz0LJvZCEgZDZD'

# AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
# AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gruwka69@gmail.com'
EMAIL_HOST_PASSWORD = 'grushka1993'
EMAIL_USE_TLS = True


""" LiqPay credentials """
LIQPAY_PUBLIC_KEY = 'i52031464220'
LIQPAY_PRIVATE_KEY = 'YZjbA8iSYTg6FtSPyT8PpZ35tr1ONYL2vCvjkgNR'
LIQPAY_DEFAULT_CURRENCY = 'UAH'
LIQPAY_DEFAULT_LANGUAGE = 'uk'
LIQPAY_DEFAULT_ACTION = 'pay'

CSRF_TRUSTED_ORIGINS = [
    'www.yakuzalviv.com'
]






