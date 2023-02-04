from django.contrib.auth import get_user_model 

from .models import Book

User = get_user_model()

def book_date_filter(user_id, from_date, to_date):
    queryset = Book.objects.select_related('records').filter(user=User.objects.get(user_id))
    queryset = queryset.filter(start__date__gt = from_date, start__date__lt=to_date)
    return queryset

def book_time_filter(user_id, from_time, to_time):
    queryset = Book.objects.select_related('records').filter(user=User.objects.get(user_id))
    queryset = queryset.filter(start__time__gt = from_time, start__time__lt=to_time)
    return queryset