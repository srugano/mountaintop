import os
from .base import *
from .base import INSTALLED_APPS, MIDDLEWARE

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "&4^s-na*^%r1y549b(#$%d0s&=#q!#0n#qde)!dp^^0io24yla"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = ("127.0.0.1",)

cwd = os.getcwd()

CACHES = {'default': {
    "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
    "LOCATION": f"{cwd}/.cache"
    }
}

try:
    from .local import *
except ImportError:
    pass
