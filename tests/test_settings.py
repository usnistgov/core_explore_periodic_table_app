""" Test Settings
"""

SECRET_KEY = "fake-key"

INSTALLED_APPS = [
    # Django apps
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django_celery_beat",
    "menu",
    # Local apps
    "tests",
    "core_main_app",
    "core_explore_common_app",
    "core_explore_keyword_app",
    "core_explore_periodic_table_app",
]

CUSTOM_NAME = "Local"
""" :py:class:`str`: Name of the local instance
"""

# IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

MIDDLEWARE = (
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core_main_app.utils.custom_context_processors.domain_context_processor",  # Needed by any curator app
                "django.template.context_processors.i18n",
            ],
        },
    },
]

ROOT_URLCONF = "tests.urls"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
MONGODB_INDEXING = False
MONGODB_ASYNC_SAVE = False
STATIC_URL = "/static/"
ENABLE_ALLAUTH = False
ENABLE_SAML2_SSO_AUTH = False
