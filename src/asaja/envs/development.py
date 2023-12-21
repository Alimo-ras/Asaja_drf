from .common import *


INSTALLED_APPS = [
    "daphne",
    "drf_spectacular",
] + INSTALLED_APPS


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "asaja",
        "USER": "asaja",
        "PASSWORD": "123@456",
        "HOST": "db",
        "PORT": "5432",
    }
}
