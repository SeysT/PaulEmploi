# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3(0$n%by47^z!bgh4ja+^ic!q+9m0bh*v5**&elcl7q56%ucv+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_WHITELIST = (
    'localhost:8080'
)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'paul_emploi_db',
        'USER': 'paul',
        'PASSWORD': 'paulpaul',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

ALLOWED_HOSTS = ['localhost']
