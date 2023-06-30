from settings import *
import os

# Configuration in PROD [insert les ip and domain authorisés]
DEBUG = os.environ['DEBUG']
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['*', '0.0.0.0', 'localhost', '127.0.0.1', 'itti-americanhighschoolmada.com']

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# if DEBUG == False:
if django.VERSION >= (4, 2):
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage"
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
        }
    }
else:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
