from pathlib import Path


# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent



# ==========================================
# SECURITY
# ==========================================

SECRET_KEY = "your-secret-key-here"

DEBUG = True

ALLOWED_HOSTS = []



# ==========================================
# INSTALLED APPS
# ==========================================

INSTALLED_APPS = [

    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",


    # Third Party Apps
    "rest_framework",
    "django_filters",

    "candidate",
    "resume",
    "job_description",
    "jos_recommend",

]




# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]



# ==========================================
# ROOT CONFIG
# ==========================================

ROOT_URLCONF = "jobrecproject.urls"



TEMPLATES = [

    {

        "BACKEND":
        "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS":
        {

            "context_processors":
            [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]



WSGI_APPLICATION = "jobrecproject.wsgi.application"



# ==========================================
# DATABASE
# ==========================================

DATABASES = {

    "default":
    {

        "ENGINE":
        "django.db.backends.sqlite3",

        "NAME":
        BASE_DIR / "db.sqlite3",

    }

}



# ==========================================
# PASSWORD VALIDATION
# ==========================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]



# ==========================================
# LANGUAGE & TIMEZONE
# ==========================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True



# ==========================================
# STATIC FILES
# ==========================================

STATIC_URL = "static/"



STATIC_ROOT = BASE_DIR / "staticfiles"



# ==========================================
# MEDIA FILES
# ==========================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"



# ==========================================
# DEFAULT PRIMARY KEY
# ==========================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)



# ==========================================
# DJANGO REST FRAMEWORK
# ==========================================

REST_FRAMEWORK = {


    "DEFAULT_RENDERER_CLASSES":
    [

        "rest_framework.renderers.JSONRenderer",

        "rest_framework.renderers.BrowsableAPIRenderer",

    ],


    "DEFAULT_FILTER_BACKENDS":
    [

        "django_filters.rest_framework.DjangoFilterBackend",

    ],


    "DEFAULT_PAGINATION_CLASS":

    "jos_recommend.pagination.JobPagination",


    "PAGE_SIZE": 10,


    "DEFAULT_PERMISSION_CLASSES":
    [

        "rest_framework.permissions.AllowAny",

    ],

}



# ==========================================
# JWT AUTHENTICATION (Optional)
# ==========================================

from datetime import timedelta


REST_FRAMEWORK.update({

    "DEFAULT_AUTHENTICATION_CLASSES":
    [

        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ]

})



SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME":
    timedelta(minutes=60),

    "REFRESH_TOKEN_LIFETIME":
    timedelta(days=1),

}