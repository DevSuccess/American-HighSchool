import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv('DEBUG', False)
if DEBUG.lower() == "true":
    DEBUG = True
else:
    DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET key is not set in environment variables")

ALLOWED_HOSTS = ['localhost', '127.0.0.1'] if DEBUG else os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

APPS = [
    "about", "accademics", "accreditation", "activity", "address",
    "blog", "contact", "home", "hour", "member", "price", "register",
    "testimonie"
]

# additional apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about.apps.AboutConfig',
    'accademics.apps.AccademicsConfig',
    'accreditation.apps.AccreditationConfig',
    'activity.apps.ActivityConfig',
    'address.apps.AddressConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'home.apps.HomeConfig',
    'hour.apps.HourConfig',
    'member.apps.MemberConfig',
    'price.apps.PriceConfig',
    'register.apps.RegisterConfig',
    'testimonie.apps.TestimonieConfig',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Web.urls'

TEMPLATES_DIRS = BASE_DIR / 'templates'
CONTEXT_APPS = ["about", "activity", "address", "contact", "hour", "member", "price", "testimonie"]

# context processors
contexts = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    "about.views_context",
    "accademics.views_context",
    "accreditation.views_context",
    "activity.views_context",
    "address.views_context",
    "blog.views_context",
    "contact.views_context",
    "home.views_context",
    "hour.views_context",
    "member.views_context",
    "price.views_context",
    "register.views_context",
    "testimonie.views_context",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': contexts,
        },
    },
]

WSGI_APPLICATION = 'Web.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'autocommit': True,
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
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

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Indian/Antananarivo'

USE_I18N = True
USE_TZ = True

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

if not DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

if DEBUG:
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage"
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
        }
    }
else:
    STORAGES = {
        "staticfiles": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
