from rest_framework.serializers import ModelSerializer, StringRelatedField,PrimaryKeyRelatedField, \
    ValidationError, SerializerMethodField
from django.db.models import Sum

from .models import Book, Record
from django.contrib.auth import get_user_model 
from .services import pages_readed_today, pages_summary, book_status
User = get_user_model()


class BookSerializer(ModelSerializer):
    user = StringRelatedField()
    pages_readed_summary = SerializerMethodField()
    pages_readed_today = SerializerMethodField()
    book_status = SerializerMethodField()
    # book_status = SerializerMethodField()
    class Meta:
        model = Book
        fields = ('id','user','title','text','pages','created_at','pages_readed_summary',\
                  'pages_readed_today','book_status')
        extra_kwargs = {
            'created_at':{'read_only':True}
        }
    
    def get_pages_readed_summary(self, obj):
        return pages_summary(obj)

    def get_pages_readed_today(self, obj):
        return pages_readed_today(obj)

    def get_book_status(self, obj):
        return book_status(obj)


class RecordSerializer(ModelSerializer):
    book = PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = Record
        fields = ('book','start', 'end', 'num_of_pages')

    def validate(self, data):

        if data['start'] >= data['end']:
            raise ValidationError("end must occur after start")
        return data