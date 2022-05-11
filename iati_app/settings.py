from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

import os

SECRET_KEY = "django-insecure-38*-=_s2(qv!k=_f7ptvoajk*47yuy_esc%al8#*ymsf6_y&08"
# DEBUG = True
DEBUG = False


def get_set_environment_config(environment_name, default_value=None):

    return os.environ.get(environment_name) or default_value


ALLOWED_HOSTS = get_set_environment_config("ALLOWED_HOSTS", default_value="*").split(
    ","
)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "corsheaders",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",
    "api",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
MIDDLEWARE += ("crum.CurrentRequestUserMiddleware",)
ROOT_URLCONF = "iati_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "iati_app.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "api.views.util.StandardResultsSetPagination",
}
APPEND_SLASH = False
MEDIA_URL = "/media/"
# Root folder to the document upload
MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded_files/")
CORS_ORIGIN_ALLOW_ALL = True


STATIC_URL = "/static/"
STATIC_PATH = os.path.join(BASE_DIR, "frontend-ui/staticfiles")
STATICFILES_DIRS = (STATIC_PATH,)
STATIC_ROOT = os.path.join(BASE_DIR, "static")
