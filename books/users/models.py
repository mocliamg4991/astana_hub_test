from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    expected_pages = models.PositiveIntegerField(blank=True, null=True)
    is_manager = models.BooleanField(default = False)