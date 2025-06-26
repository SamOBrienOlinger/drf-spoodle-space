from pathlib import Path
import os
import re
import dj_database_url
import urllib.parse

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

BASE_DIR = Path(__file__).resolve().parent.parent

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        (
            'rest_framework.authentication.SessionAuthentication'
            if os.environ.get('DEV') == 'True' # Check if DEV is explicitly 'True'
            else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
        )
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}

if os.environ.get('DEV') != 'True': # Check if DEV is explicitly NOT 'True'
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'spoodle_space.serializers.CurrentUserSerializer'
}

SECRET_KEY = os.environ.get('SECRET_KEY')

# --- DEBUG SETTING ---
# Set DEBUG to True if DEV is 'True' in env.py, otherwise False for production.
DEBUG = os.environ.get('DEV') == 'True'

# --- ALLOWED_HOSTS ---
# Dynamically pull hosts from env.py and include production Heroku host.
# Extract only the hostname from CLIENT_ORIGIN_DEV for ALLOWED_HOSTS
gitpod_host = os.environ.get('CLIENT_ORIGIN_DEV')
if gitpod_host:
    # urlparse breaks down the URL. .netloc gets the 'hostname:port' part.
    # .split(':')[0] removes the port if present (e.g., '8000-...' from the hostname itself)
    parsed_gitpod_host = urllib.parse.urlparse(gitpod_host).netloc.split(':')[0]
else:
    parsed_gitpod_host = None # Set to None if CLIENT_ORIGIN_DEV is not found

ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),      # 'localhost' from env.py
    parsed_gitpod_host,                  # The extracted hostname (e.g., '8000-samobrienol-drfspoodles-gxrj9dlvoz2.ws-eu120.gitpod.io')
    'spoodle-space-pp5.herokuapp.com',   # Heroku production app URL
    'spoodlespace.herokuapp.com',
    'localhost',
    '127.0.0.1',
]

# Filter out any None or empty string values that might result from missing env vars
# ALLOWED_HOSTS = [host for host in ALLOWED_HOSTS if host]

# --- CORS_ALLOWED_ORIGINS ---
# Dynamically pull origins from env.py and include production Heroku origin.
CORS_ALLOWED_ORIGINS = list(filter(None, [
    'https://spoodle-space-pp5.herokuapp.com',
    'http://localhost:3000',
    os.environ.get('CLIENT_ORIGIN'),
    os.environ.get('CLIENT_ORIGIN_DEV'),
    "https://3000-samobrienol-spoodlespac-93mpe3hepff.ws-eu120.gitpod.io",
]))

# CORS_ALLOWED_ORIGINS = [
#     'https://spoodle-space-pp5.herokuapp.com',
#     'http://localhost:3000',
#     os.environ.get('CLIENT_ORIGIN'),
#     os.environ.get('CLIENT_ORIGIN_DEV'),
#     "https://3000-samobrienol-spoodlespac-93mpe3hepff.ws-eu120.gitpod.io",
# ]

CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'

CSRF_TRUSTED_ORIGINS = [
    "https://spoodle-space-pp5.herokuapp.com",
    "http://localhost:3000",
    "https://3000-samobrienol-spoodlespac-93mpe3hepff.ws-eu120.gitpod.io",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    'profiles',
    'posts',
    'comments',
    'likes',
    'followers',
    'dogprofiles',
    'doghealth',
    'dogdanger',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spoodle_space.urls'

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

WSGI_APPLICATION = 'spoodle_space.wsgi.application'

# --- DATABASES CONFIGURATION (CRITICAL FIX) ---
# Get the DATABASE_URL environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL: # This will be true if env.py loads DATABASE_URL
    # If DATABASE_URL is set, parse it.
    # dj_database_url.parse expects a string.
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL) # <-- REMOVED .encode('utf-8')
    }
else:
    # Fallback to SQLite for local development if DATABASE_URL is not found
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'