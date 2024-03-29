import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ADMINS = [("admin", os.getenv("SUPER_USER_EMAIL", ""))]

ADMIN_SITE_HEADER = "easypolitics"
ADMIN_SITE_INDEX_TITLE = "Site administration"
ADMIN_SITE_TITLE = "easypolitics"

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

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
}

CONGRESS_VERSION = "118"

# https://github.com/adamchainz/django-cors-headers
CORS_URLS_REGEX = r"^/v1/.*$"

CSRF_COOKIE_HTTPONLY = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EXCLUDE_BILLS = ["hres", "sres"]

HOUSE_BILLS = ["hconres", "hjres", "hr", "hres"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "backend.bills",
]

LANGUAGE_CODE = "en-us"

MANAGERS = ADMINS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

PROPUBLICA_API = os.getenv("PROPUBLICA_API")

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
    ),
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle"
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "1000/day",
        "user": "1000/day",
    },
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
    "NON_FIELD_ERRORS_KEY": "error",
    "EXCEPTION_HANDLER": "config.exceptions.custom_exception_handler",
}

ROOT_URLCONF = "config.urls"

SECURE_BROWSER_XSS_FILTER = True

SENATE_BILLS = ["s", "sconres", "sjres", "sres"]

SESSION_COOKIE_HTTPONLY = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = "/app/static"
STATIC_URL = "static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

WSGI_APPLICATION = "config.wsgi.application"

X_FRAME_OPTIONS = "DENY"
