import os
from logging.config import dictConfig

from celery import Celery
from celery.schedules import crontab
from celery.signals import setup_logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

app = Celery('warehouses', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    broker_url=os.environ.get("CELERY_BROKER_URL", default="redis://redis:6379/0"),
    timezone="Europe/Moscow",
    accept_content=["json"],
    task_serializer="json",
    task_time_limit=5 * 60,
    task_soft_time_limit=60,
    include=["warehouses.tasks"],
    broker_transport_options={"max_retries": 3, "visibility_timeout": 60 * 60 * 5},
    worker_prefetch_multiplier=1,  # Disable prefetching, it's causes problems and doesn't help performance
)

app.autodiscover_tasks()
beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"


app.conf.task_routes = {
    "warehouses.tasks.get_the_quote_of_the_day": {"queue": "worker", "routing_key": "worker"},

}

app.conf.beat_schedule = {
    "get_the_quote_of_the_day": {
        "task": "warehouses.tasks.get_the_quote_of_the_day",
        "schedule": crontab(minute="*/1"),
    },
}


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"verbose": {"format": "%(asctime)s [%(levelname)s] %(message)s"}},
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "celery": {"level": "INFO", "handlers": ["console"], "propagate": True},
    },
}


@setup_logging.connect
def setup_loggers(*args, **kwargs):
    dictConfig(LOGGING_CONFIG)
