import os
from pathlib import Path
from dotenv import load_dotenv
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    
    "drf_2fa",
    "user",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drf_2fa_project.urls'

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

WSGI_APPLICATION = 'drf_2fa_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

AUTHENTICATION_BACKENDS = ["user.backends.AuthBackend"]
AUTH_USER_MODEL = "user.UserAccount" # Custom User Model

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DRF_2FA_SETTINGS = {
    "OTP_BACKEND": "drf_2fa.backends.authenticator.AuthenticatorAppOTPBackend",
    "TWILIO_ACCOUNT_SID": os.environ.get("TWILIO_ACCOUNT_SID", ""),
    "TWILIO_AUTH_TOKEN": os.environ.get("TWILIO_AUTH_TOKEN", ""),
    "TWILIO_NUMBER": os.environ.get("TWILIO_NUMBER", ""),
    "OTP_LENGTH": 8,
    "OTP_EXPIRE": datetime.timedelta(seconds=86400),
    "OTP_EMAIL_FROM": "noreply@gmail.com",
    "SHOW_OTP_MODEL_ADMIN": True,
}

from .admin import *