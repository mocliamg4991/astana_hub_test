from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import F
from .serializers import BookSerializer, RecordSerializer
from .models import Book, Record
from .permissions import IsOwner

class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = BookSerializer
    permission_classes = (IsOwner|IsAdminUser,)

    def get_queryset(self):
        if self.request.user.is_staff is False:
            queryset = Book.objects.select_related('user').filter(user=self.request.user)
        else:
            queryset = Book.objects.select_related('user')
        return queryset


    def perform_create(self, serializer):
        return serializer.save(
                    user=self.request.user
                )

class RecordViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = RecordSerializer
    
    def get_queryset(self):
        queryset = Record.objects.all()
        return queryset


    
