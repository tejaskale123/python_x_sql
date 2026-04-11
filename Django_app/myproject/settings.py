from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')
DB_ENGINE = os.getenv('DB_ENGINE', 'sqlite').lower()

SECRET_KEY = 'django-insecure-tczb^mj1968=@q9cx=mxenn82!s=-mxud%p-%#1u-6v071n9dk'

DEBUG = os.getenv('DEBUG', 'True').strip().lower() in ('1', 'true', 'yes')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# 🔥 APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig',
    
    'rest_framework',
]


# 🔥 MIDDLEWARE (same ठेव)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'myproject.urls'


# 🔥 TEMPLATES (IMPORTANT CHANGE)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        # 👇 हे add केलं (global templates folder)
        'DIRS': [BASE_DIR / "templates"],  

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


WSGI_APPLICATION = 'myproject.wsgi.application'


# 🔥 DATABASE (supports SQLite by default; enable MySQL with DB_ENGINE=mysql)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}

# 🔥 STATIC FILES (CSS setup)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 👇 NEW (IMPORTANT)
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'AUTH_HEADER_TYPES': ('Bearer',),
}