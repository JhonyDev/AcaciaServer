import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env_file = os.path.join(BASE_DIR, ".env")

env = environ.Env()
env.read_env(env_file)

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG', cast=bool)

PRODUCTION = env('PRODUCTION', cast=bool)

ALLOWED_HOSTS = ['*']

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'api.apps.ApiConfig',
    'admin_panel.apps.AdminPanelConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'rest_framework',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AcaciaServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AcaciaServer.wsgi.application'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myproject',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
#     '/Jhony Dev/PycharmProjects/AcaciaServer/static'
# )
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')

CONSUMER_KEY = env('CONSUMER_KEY')
CONSUMER_SECRET = env('CONSUMER_SECRET')
PASSKEY = env('PASSKEY')
SHORT_CODE = env('SHORT_CODE')
CALLBACK_URL = env('CALLBACK_URL')
