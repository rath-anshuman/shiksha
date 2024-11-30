from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import AccountManager
from django.utils import timezone

class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30, blank=True)
    regno = models.CharField(max_length=15, unique=True)
    section = models.CharField(max_length=5, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'regno'  
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.regno
