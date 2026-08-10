from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-!e=l%7)wwatw(njjw_3=-940!r$*6crdlobdhe28b^ourre6mw'

DEBUG = True

ALLOWED_HOSTS = []



# ==========================
# Applications
# ==========================
INSTALLED_APPS = [

    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "rest_framework",
    "rest_framework_simplejwt",

    # Local apps
    "accounts",
    "recruiters",
]


# Custom User Model
AUTH_USER_MODEL = "accounts.User"




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



# ==========================
# Templates
# ==========================

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





# ==========================
# Database
# ==========================

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





# ==========================
# Django REST Framework
# ==========================

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