from .settings import *
DATABASES = {
    'default': dj_database_url.config()
}
ALLOWED_HOSTS=['*']
DEBUG = False