"""Isolated automated tests. Never connects to the configured hosted database."""
from .settings import *
import os
import dj_database_url
import tempfile
import atexit
import shutil

SECRET_KEY = 'spoodlespace-isolated-tests-only'
DATABASES = {'default': dj_database_url.parse(os.environ['TEST_DATABASE_URL']) if os.environ.get('TEST_DATABASE_URL') else {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = tempfile.mkdtemp(prefix='spoodle-tests-')
atexit.register(shutil.rmtree, MEDIA_ROOT, ignore_errors=True)
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1']
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
