from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import AccountManager
from django.utils import timezone

class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    date_joinee = models.DateTimeField(default=timezone.now)
    # No need to redefine password field, as AbstractBaseUser handles it
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_accounts',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
