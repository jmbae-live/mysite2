"""
Django settings for mysite2 project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from django.utils.translation import gettext_lazy as _

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+5pyu10r9jecf%pk8!ix_q!ap^0^#8^+%8-80+o#wbv7$h#ull"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# https 서버 실행을 위해 할 일
# 1. 운영체제의 hosts 파일 수정 (mysite.com 127.0.0.1 추가)
# 2. ALLOWED_HOSTS mysite.com 추가
ALLOWED_HOSTS = [
    'mysite.com', 'localhost', '127.0.0.1'
]

# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'social_django',  # 소셜 로그인 앱 (pip install social-auth-app-django )
    'django_extensions',  # runserver_plus 실행 (pip install django-extensions)
    "shop.apps.ShopConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "blog.apps.BlogConfig",
    "taggit",
    "rosetta",
    "parler",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / 'templates',
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "shop.context_processor.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite2.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mysite2",
        "USER": "mysite2",
        "PASSWORD": "1234",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SESSION_REDIS_ALIAS = "default"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

CELERY_TASK_ALWAYS_EAGER = DEBUG

# 소셜 로그인 백엔드 설정
AUTHENTICATION_BACKENDS = [
    'social_core.backends.naver.NaverOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# 네이버 소셜 로그인 설정
SOCIAL_AUTH_NAVER_KEY = 'JiARA_lKm_5xm9Sd9l4x'
SOCIAL_AUTH_NAVER_SECRET = 'TXMPVDfEVC'

# 네이버 소셜 로그인 데이터 범위
SOCIAL_AUTH_NAVER_EXTRA_DATA = ['profile_image']

# 소셜 로그인 JSON Field 추가 ( Postgres 경우 )
SOCIAL_AUTH_JSONFIELD_ENABLED = True

LANGUAGES = [
    ('en', _('English')),
    ('ko', _('Korean')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'ko'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

LOGIN_REDIRECT_URL = 'home'
