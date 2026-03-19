from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("TEST_POSTGRES_DB", default="storaging_db"),
        "USER": env("TEST_POSTGRES_USER", default="admin"),
        "PASSWORD": env("TEST_POSTGRES_PASSWORD", default="password"),
        "HOST": env("TEST_POSTGRES_HOST", default="0.0.0.0"),
        "PORT": env("TEST_POSTGRES_PORT", default="5439"),
        "TEST": {
            "NAME": "mytestdatabase",
        },
    },
}

# django setting.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://0.0.0.0:6379/0",
    }
}
