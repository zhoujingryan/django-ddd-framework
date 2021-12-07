import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = True

INSTALLED_APPS = ["django_ddd_framework", "tests.ddd.apps.DDDConfig"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # in memory
    }
}
LANGUAGE_CODE = "en-us"
