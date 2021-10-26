from django.db import models


class Room(models.Model):
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
