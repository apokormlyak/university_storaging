from django.http import HttpResponse

from ..models import Quotes
from ..tasks import get_the_quote_of_the_day
from django import template

register = template.Library()


@register.simple_tag
def quote_of_the_day(request=None):
    get_the_quote_of_the_day()
    quote = getattr(Quotes.objects.last(), "quote")
    author = getattr(Quotes.objects.last(), "author")
    return f'{quote} (c) {author}'
