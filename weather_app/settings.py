"""
Django settings for weather_app project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v-a_mnnf7)4e3fvstgy66)_^3#f7vqk-_d=p04443_uyvr-vf4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost',
            '127.0.0.1',
            'django-app',
            'my-django-app-latest-56ef.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weather',
    'rest_framework',
    # The following apps are required:
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'drf_yasg',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add this line
]


ROOT_URLCONF = 'weather_app.urls'

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

WSGI_APPLICATION = 'weather_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    #"""""" Set up for connecting with desktop db service """""
    # 'default': {
    #     # 'ENGINE': 'django.db.backends.sqlite3',
    #     # 'NAME': BASE_DIR / 'db.sqlite3',
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'weather_db_1',  # Name of your database
    #     'USER': 'root',          # MySQL username
    #     'PASSWORD': 'saifch',    # MySQL password
    #     'HOST': '127.0.0.1',     # Use 'localhost' for local MySQL server
    #     'PORT': '3309',          # Default MySQL port
    # }

    #"""""" Set up for connecting with containerized db service """""
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'weather_db_1', 
    #     'USER': 'user',         
    #     'PASSWORD': 'saifch',    
    #     'HOST': 'db',             
    #     'PORT': '3306',
    # }

    #"""""" Set up for connecting with cloud db service """"""
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'sql12759022',  
    #     'USER': 'sql12759022',         
    #     'PASSWORD': 'XDFyPtjuM8',    
    #     'HOST': 'sql12.freesqldatabase.com', 
    #     'PORT': '3306',               
    # }
    'default': {
        'ENGINE': 'django_snowflake',
        'NAME': 'WEATHER_DB',
        'SCHEMA': 'PUBLIC',
        'USER': 'SAIF',
        'PASSWORD': 'Hayouta123456',
        'ACCOUNT': 'RAHLBXI-TK36461',
        'WAREHOUSE': 'COMPUTE_WH',
    }
}




SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://127.0.0.1:8000/accounts/google/login/callback/'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '158935204339-uqug360hjf9b89h1t8qtcvmg2tj25k31.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Needed to login by username in Django admin, regardless of `allauth`
    'allauth.account.auth_backends.AuthenticationBackend',  # `allauth` specific authentication methods, such as login by email
]



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = "dashboard"


STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Directory to collect static files for production (optional for development)
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Or another path where you store static files during development
]

# Set Up DRF in settings.py: Add a basic DRF configuration (optional)
# configured to enforce authentication and permissions for all API endpoints. 
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # Add this line
    'PAGE_SIZE': 10,  # to set the default page size
}
