"""
Django settings for HeyLiseli project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ovklzskoud(9ju*%=k39rpk8b(5*@%a&1r0)a7^g3majl9=bkp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'social_django',
    'catalog',
    'registration',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', #Debug toolbar
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'HeyLiseli.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'HeyLiseli.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Custom user model declaration
AUTH_USER_MODEL = 'catalog.Liseli'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, 'static/')
COMPRESS_ENABLED=True
STATICFILES_FINDERS=(
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


#Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL="/media/"

#Registration settings:
ACCOUNT_ACTIVATION_DAYS=8
REGISTRATION_AUTO_LOGIN=True
LOGIN_REDIRECT_URL="/"
REGISTRATION_FORM="catalog.forms.registerForm"
REGISTRATION_EMAIL_HTML=True


#Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='heyliseligenc@gmail.com'
EMAIL_HOST_PASSWORD='liseliaydavebogi'
EMAIL_PORT=587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'HeyLiseli@genc.com'


#Social Auth Backend
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/social-registry/'

#Twitter auth
SOCIAL_AUTH_TWITTER_KEY = '0HhwSzB6sdy1dvuwIMaYomWcV'
SOCIAL_AUTH_TWITTER_SECRET = 'QsyhkMPCLK0YFaWWUiUoSSy0ifRJtR5byW6zC0jKrkkkTKrTNR'

#Facebook auth
SOCIAL_AUTH_FACEBOOK_KEY = '1367123683406776'
SOCIAL_AUTH_FACEBOOK_SECRET = 'edd4ff84ce4aa9e1255eb6f44edd8ac0'

#Google auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ="227583987065-u4qc27kikmgq0qdgmh0ord97prq5ui31.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ="DGsAfKYIaw6ImRAOUbU1N8Zx"
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
    'https://www.googleapis.com/auth/plus.login',
    'https://www.googleapis.com/auth/userinfo.email',
]

#Session settings
SESSION_SAVE_EVERY_REQUEST = True

#Django Debug Toolbar
INTERNAL_IPS = ('127.0.0.1',)