from django.db import models
from django.conf import settings

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField(blank=True, null=True)
    pages = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Record(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='records')
    start = models.DateTimeField()
    end = models.DateTimeField()
    num_of_pages = models.PositiveIntegerField()

    def __str__(self):
        return 'Запись {0} Книги - {1}'.format(self.id, self.book.title)