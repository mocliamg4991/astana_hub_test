from django.contrib.auth import get_user_model 
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import UserRegisterSerializer, UserSerializer
from .permissions import IsManager

User = get_user_model()

class UserRegisterViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser|IsManager,)
    
    def get_queryset(self):
        if self.request.user.is_manager is True:
            queryset = User.objects.exclude(is_staff = True)
        else:
            queryset = User.objects.all()
        return queryset
    