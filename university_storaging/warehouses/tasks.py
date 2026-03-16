import requests
from settings.celery import app
import logging
from django.core.cache import caches
from .models import Quotes

logger = logging.getLogger(__name__)
cache = caches['default']


@app.task(bind=True, max_retries=3, soft_time_limit=86400, time_limit=90000)
def get_the_quote_of_the_day(self):
    logger.info("[TASK] Start getting the quote of the day")
    url = 'https://favqs.com/api/qotd'
    session = requests.Session()
    quote_of_the_day = session.get(url=url).json()['quote']
    obj = Quotes.objects.create(
        quote=quote_of_the_day['body'],
        author=quote_of_the_day['author'],
    )
    cache.set('quote', quote_of_the_day['body'])
    cache.set('author', quote_of_the_day['author'])
    logger.info("[TASK] The quote of the day saved")
