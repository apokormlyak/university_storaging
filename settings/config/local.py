from .base import *
import dj_database_url

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://{0}:{1}@{2}:{3}/{4}".format(
            env("DJANGO_POSTGRES_USER", default="admin"),
            env("DJANGO_POSTGRES_PASSWORD", default="password"),
            env("DJANGO_POSTGRES_HOST", default="postgres"),
            env("DJANGO_POSTGRES_PORT", default="5432"),
            env("DJANGO_POSTGRES_DB", default="storaging_db"),
        ),
    )
}
# django setting.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379/0",
    }
}
