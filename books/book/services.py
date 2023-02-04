from datetime import datetime
from django.db.models import Sum

from .models import Book

# def get_book_status():
#     Book.objects.select_related('')

def pages_readed_today(obj):
    return obj.records.filter(start__date=datetime.now().date()).aggregate(pages = \
        Sum('num_of_pages'))

def pages_summary(obj):
    return obj.records.aggregate(pages = Sum('num_of_pages'))

def book_status(obj):
    status = ''
    if isinstance(obj.user.expected_pages, int):
        if obj.user.expected_pages <= pages_readed_today(obj).get('pages'):
            status = 'green'
        else:
            status = 'red'
    else:
        status = 'set expected_pages in settings'
    return status