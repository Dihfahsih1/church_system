
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dfi)!n=vat#4_8*#5t=8pfa-)jo*#gmn^b16&v)o@%pq*8&&&c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'canonapp',
    'accounts',
    'crispy_forms',
    'import_export',
    'twilio',
    'reportlab',
    'xhtml2pdf',
]

#AUTH_USER_MODEL = 'canonapp.User'


#AUTH_USER_MODEL='receptionistapp.User'  #changes the built in user to ours

MIDDLEWARE = [
    'CanonInventory.middleware.LoginRequiredMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CanonInventory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'CanonInventory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#              'default': {
#                 'ENGINE': 'django.db.backends.postgresql',
#                 'NAME': 'canon_inventory_db',
#                 'USER': 'postgres',
#                 'PASSWORD': '1234',
#                 'HOST': '127.0.0.1',
#                 'PORT': '5432',
#             }
#         }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}





# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CRISPY_TEMPLATE_PACK='bootstrap4'

IMPORT_EXPORT_USE_TRANSACTIONS = True

LOGIN_REDIRECT_URL = '/account/login_success/'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025


LOGIN_URL = '/account/login/'

LOGIN_EXEMPT_URLS = (
    'logout/',
    'canonapp/operations_edit_car',
    'canonapp/operations_edit_driver',
    'account/reset_password/',
    'account/reset_password_done',
    'account/reset_password_confirm',
    'account/reset_password_complete',

)


SESSION_COOKIE_AGE = 60 * 10  # Session will expiry after 10 minutes idle.
SESSION_SAVE_EVERY_REQUEST = True