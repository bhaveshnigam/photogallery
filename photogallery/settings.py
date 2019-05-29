"""
Django settings for photogallery project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_q40bfrt)ga_1jxli5bg7zua10$1s9+vgoz@z#p)#b^&@5xiak'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['bhaveshpi.local', 'localhost', '10.8.0.3']


# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'haystack',
    'elasticstack',
    'memoize',

    'photologue',
    'sortedm2m',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'photogallery.urls'


# from photologue import PHOTOLOGUE_APP_DIR
# TEMPLATE_DIRS = (
#     PHOTOLOGUE_APP_DIR
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'photogallery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public', 'static').replace('\\', '/'),
)


MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')
MEDIA_URL = '/media/'




ELASTICSEARCH_DEFAULT_NGRAM_SEARCH_ANALYZER = 'standard'


# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'elasticstack.backends.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'photogallery',
    },
}


DEFAULT_CACHE_TIMEOUT = 1 * 24 * 60 * 60


# Keep this at bottom of file
try:
    from photogallery.local_settings import *
except ImportError:
    pass

def show_toolbar(request):
    return True

# Enabling debug-toolbar settings. Should be after local settings import.
# if DEBUG:
    # # MIDDLEWARE_CLASSES.append('common.middleware.NonHtmlDebugToolbarMiddleware')
    # MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.common.CommonMiddleware'), 'debug_toolbar.middleware.DebugToolbarMiddleware')
    # INSTALLED_APPS.append('debug_toolbar')
    # INSTALLED_APPS.append('template_profiler_panel')
    # DEBUG_TOOLBAR_PATCH_SETTINGS = False
    # DEBUG_TOOLBAR_PANELS = [
    #   'debug_toolbar.panels.versions.VersionsPanel',
    #   'debug_toolbar.panels.timer.TimerPanel',
    #   'debug_toolbar.panels.settings.SettingsPanel',
    #   'debug_toolbar.panels.headers.HeadersPanel',
    #   'debug_toolbar.panels.request.RequestPanel',
    #   'debug_toolbar.panels.sql.SQLPanel',
    #   'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    #   'debug_toolbar.panels.templates.TemplatesPanel',
    #   'debug_toolbar.panels.cache.CachePanel',
    #   'debug_toolbar.panels.signals.SignalsPanel',
    #   # 'template_profiler_panel.panels.template.TemplateProfilerPanel',
    #   'debug_toolbar.panels.logging.LoggingPanel',
    #   'debug_toolbar.panels.redirects.RedirectsPanel',
    # ]
    # DEBUG_TOOLBAR_CONFIG = {
    #     'SHOW_TOOLBAR_CALLBACK': show_toolbar
    # }
