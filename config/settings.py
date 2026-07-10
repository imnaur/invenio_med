import os
from pathlib import Path

from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv(override=True)
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv("SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "catalog",
    "users",
    "appointments",
    "pages.apps.PagesConfig",
    "blog",
    "chatbot",
    "crispy_forms",
    "crispy_bootstrap5",
    "celery",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

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

LANGUAGE_CODE = "ru"
LANGUAGES = [
    ("ru", "Russian"),
    ("en", "English"),
]


def gettext(s):
    return s


MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"
USE_I18N = True

USE_L10N = True
TIME_ZONE = "UTC"
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

AUTH_USER_MODEL = "users.CustomUser"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ______________________MailSend_________________

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_USE_SSL = False
LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "users:profile"

REDIS_HOST = os.getenv("REDIS_HOST")
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:6379/0"

CELERY_BEAT_SCHEDULE = {
    "send-appointment-reminders-every-day": {
        "task": "appointments.tasks.check_upcoming_appointments",
        "schedule": crontab(hour=9, minute=0),  # Каждое утро в 9:00
    },
}
