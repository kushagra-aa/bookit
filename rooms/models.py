from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User


# Create your models here.

# class User(AbstractBaseUser, PermissionsMixin):
#     # username=None;
#     email = models.EmailField(("email address"), unique=True)
#     name = models.CharField(max_length=75)
#     is_seller = models.BooleanField(default=False)
#     contact = models.CharField(max_length=10)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


class room(models.Model):
    # model for rooms
    def __str__(self) -> str:
        return self.address
    room_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, default="null")
    room_size = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    rate = models.IntegerField(default=0)
    floor = models.CharField(max_length=5, default="null")
    furnishing = models.CharField(max_length=25, default="null")
    area = models.CharField(max_length=50, default="null")
    parking = models.CharField(max_length=25, default="null")
    description = models.CharField(max_length=255)
    seller_id = models.CharField(default="null", max_length=20)
