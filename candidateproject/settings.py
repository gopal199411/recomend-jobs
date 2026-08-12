from pathlib import Path


<<<<<<< HEAD
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-!e=l%7)wwatw(njjw_3=-940!r$*6crdlobdhe28b^ourre6mw'

DEBUG = True

ALLOWED_HOSTS = []



=======
# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Security
SECRET_KEY = "change-this-to-your-own-secret-key"
DEBUG = True
ALLOWED_HOSTS = []


>>>>>>> e2ad693 (commit msg)
# ==========================
# Applications
# ==========================
INSTALLED_APPS = [
<<<<<<< HEAD

=======
>>>>>>> e2ad693 (commit msg)
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

<<<<<<< HEAD
    # Third party
    "rest_framework",
    "rest_framework_simplejwt",
=======
    # Third-party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
>>>>>>> e2ad693 (commit msg)

    # Local apps
    "accounts",
    "recruiters",
]


# Custom User Model
AUTH_USER_MODEL = "accounts.User"


<<<<<<< HEAD


# ==========================
# Middleware
# ==========================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]




ROOT_URLCONF = 'candidateproject.urls'

=======
# ==========================
# Middleware
# ==========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "candidateproject.urls"
>>>>>>> e2ad693 (commit msg)


# ==========================
# Templates
# ==========================
<<<<<<< HEAD

TEMPLATES = [
    

    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS':
        {

            'context_processors':

            [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]



WSGI_APPLICATION = 'candidateproject.wsgi.application'



=======
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


WSGI_APPLICATION = "candidateproject.wsgi.application"
>>>>>>> e2ad693 (commit msg)


# ==========================
# Database
# ==========================
<<<<<<< HEAD

DATABASES = {

    'default':

    {

        'ENGINE':
        'django.db.backends.sqlite3',

        'NAME':
        BASE_DIR / 'db.sqlite3',

    }

}





# ==========================
# Password Validation
# ==========================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]





# ==========================
# Language
# ==========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True





# ==========================
# Static & Media
# ==========================

STATIC_URL = 'static/'


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'





# ==========================
# Email OTP Development
# ==========================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)


DEFAULT_FROM_EMAIL = (
    "noreply@example.com"
)




=======
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==========================
# Password Validation
# ==========================
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


# ==========================
# Language and Timezone
# ==========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True


# ==========================
# Static and Media Files
# ==========================
STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==========================
# Email OTP – Gmail SMTP
# ==========================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "airesumebuilderandscreeningsys@gmail.com"
EMAIL_HOST_PASSWORD = "gdkdwhshswrbsjlc"

DEFAULT_FROM_EMAIL = "AI Resume Builder and Screening System <airesumebuilderandscreeningsys@gmail.com>"
>>>>>>> e2ad693 (commit msg)

# ==========================
# Django REST Framework
# ==========================
<<<<<<< HEAD

REST_FRAMEWORK = {


    "DEFAULT_AUTHENTICATION_CLASSES":

    (

        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ),



    "DEFAULT_PERMISSION_CLASSES":

    (

        "rest_framework.permissions.IsAuthenticated",

    ),

}
=======
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}


# Default primary key type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
>>>>>>> e2ad693 (commit msg)
