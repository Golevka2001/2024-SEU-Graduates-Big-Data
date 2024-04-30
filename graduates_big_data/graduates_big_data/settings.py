"""
Django settings for graduates_big_data project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%3e#@30!w*+90b5rn9vo*hcb3^^2vty5-()a=yb)bijmhq!$r%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

ENABLE_CAS = False

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "health_check",
    "django_cas_ng",
    "stat_data",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_cas_ng.middleware.CASMiddleware",
]

AUTHENTICATION_BACKENDS = [
    # "django.contrib.auth.backends.ModelBackend",
    "django_cas_ng.backends.CASBackend",
]

ROOT_URLCONF = "graduates_big_data.urls"

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

WSGI_APPLICATION = "graduates_big_data.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": os.path.join(BASE_DIR, "my.cnf"),
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "stat_data", "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CAS settings
# Testing CAS server
CAS_LOGIN_URL = "https://apitest.seu.edu.cn/dist/#/dist/main/login"
CAS_SERVICE_VALIDATE_URL = "https://apitest.seu.edu.cn/auth/casapi/serviceValidate"
CAS_LOGOUT_URL = "https://apitest.seu.edu.cn/dist/#/dist/logOut"

# Production CAS server
# CAS_LOGIN_URL = "https://auth.seu.edu.cn/dist/#/dist/main/login"
# CAS_SERVICE_VALIDATE_URL = "https://auth.seu.edu.cn/auth/casapi/serviceValidate"
# CAS_LOGOUT_URL = "https://auth.seu.edu.cn/dist/#/dist/logOut"

CAS_SERVICE_URL = "https://gradudata2024.seu.edu.cn"
CAS_LOGIN_NEXT_PAGE = "/"
CAS_LOGOUT_NEXT_PAGE = "/"
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_USERNAME_ATTRIBUTE = "mainCardId"
