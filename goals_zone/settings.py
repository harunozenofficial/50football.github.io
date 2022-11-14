# noinspection GrazieInspection
"""
Django settings for goals.zone project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from warnings import filterwarnings

filterwarnings("ignore", message=r".*received a naive datetime")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "4&h7em$riknyt&y!@9!w@j%d&3s+0gz&xq%p01jw@3g#8p_ixr")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("SECRET_KEY") is not None else True

ADMINS = [("André Meneses", "andre@meneses.pt")]
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

ALLOWED_HOSTS = ["goals.zone", "goals.africa", ".meneses.pt", "127.0.0.1", "localhost"]

CSRF_TRUSTED_ORIGINS = [
    "https://goals.zone",
    "https://goals.africa",
    "https://*.meneses.pt",
    "http://127.0.0.1",
    "http://localhost",
]

CORS_ALLOWED_ORIGINS = [
    "https://goals.zone",
    "https://goals.africa",
    "https://gzreact.meneses.pt",
    "https://gz.meneses.pt",
    "https://videogoals.meneses.pt",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "background_task",
    "matches.apps.MatchesConfig",
    "msg_events.apps.MsgEventsConfig",
    "monitoring.apps.MonitoringConfig",
    "corsheaders",
    "ner.apps.NerConfig",
    "rest_framework",
    "rangefilter",
    "django_hosts",
    "django_logtail",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django_hosts.middleware.HostsRequestMiddleware",
    "goals_zone.middleware.timezone.TimezoneMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_hosts.middleware.HostsResponseMiddleware",
]

ROOT_URLCONF = "goals_zone.urls"
ROOT_HOSTCONF = "goals_zone.hosts"
DEFAULT_HOST = "goals_zone"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "goals_zone.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
        "TIMEOUT": 30,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "matches.pagination.OnlyDataLimitOffsetPagination",
    "PAGE_SIZE": 50,
}

LOGTAIL_FILES = {
    "Background Tasks": "/home/goals_zone/logs/background_tasks.log",
    "Background Tasks Errors": "/home/goals_zone/logs/background_tasks-error.log",
    "Gunicorn": "/home/goals_zone/logs/gunicorn-error.log",
    "goals.zone": "/home/goals_zone/logs/goals_zone.log",
    "goals.zone Errors": "/home/goals_zone/logs/goals_zone-error.log",
    "nginx Access": "/home/goals_zone/logs/nginx-access.log",
    "nginx Errors": "/home/goals_zone/logs/nginx-error.log",
    "Supervisor": "/var/log/supervisor/supervisord.log",
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

INTERNAL_IPS = "127.0.0.1"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Settings for background tasks
MAX_ATTEMPTS = 60
MAX_RUN_TIME = 300
# Doesn't seem to be working when True
BACKGROUND_TASK_RUN_ASYNC = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-file<s/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_URL = "/static/"
STATIC_ROOT = os.environ.get("STATIC_ROOT")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

NER_MODEL_FOLDER = os.path.join(BASE_DIR, "ner/goals_zone_model")

GEOIP_PATH = os.path.join(
    STATICFILES_DIRS[0] if DEBUG else STATIC_ROOT, "geoip2/GeoLite2-City.mmdb"
)

PREMIUM_PROXY = os.environ.get("PREMIUM_PROXY")
