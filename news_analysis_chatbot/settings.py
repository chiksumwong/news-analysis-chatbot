"""
Django settings for news_analysis_chatbot project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Line Message API
# LINE_CHANNEL_SECRET = '979627ceddbe834054c388c19f908b7f'
# LINE_CHANNEL_ACCESS_TOKEN = 'Ij1FUOCJYNTxxQAaFLZC2ev3vXgyRxab3pwhEjjOJD5QvtugSgOkFETDZi/nJoce7/jG/3mZVBFY5g6LJxprBdJHPEZMqVUKahDtFVBl8xkzgF7Ht8D8XIaJcKB1BsMsRlCCJ45RWGNoi496B0MtfgdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = 'd0879dc88ae6a1df6e094125bf35e954'
LINE_CHANNEL_ACCESS_TOKEN = 'EKkOL15VVHoxSfnyczwGnoIXGEgCJTZD7zHX+VUWhNzs3JRnkOZpHARNGocSp/+5q6mnl3M8rdRz0xSOaTirx/p25XVqZ9Y8Kn3t3sOZzKljEClnTFHvWFcJHypJIBArEUl+Rm6WE8yUP7QX18ed0gdB04t89/1O/w1cDnyilFU='



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9+j22cn)=+gp=j1*91c=5*6sz1s7s_!g+7pto=@g$bb=+$ie_r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'news-analysis-chatbot.herokuapp.com',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party Apps
    'corsheaders',
    'rest_framework',

    # Local Apps
    'chatbot',
    'news',
    'account'
]

MIDDLEWARE = [
    # Third-Party
    'corsheaders.middleware.CorsMiddleware',
    # Django
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'news_analysis_chatbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'news_analysis_chatbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # local sqlite3 database
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # Heroku Postgres Database
    'production': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'




# Django REST Framework Setting
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# CORS
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
]
    
JWT_AUTH = {
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

import django_heroku
# Activate Django-Heroku.
django_heroku.settings(locals())