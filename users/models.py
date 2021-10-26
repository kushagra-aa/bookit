from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomAccountManager


class MyUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(("email address"), unique=True)
    name = models.CharField(max_length=75)
    is_seller = models.BooleanField(default=False)
    contact = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
