from django.contrib import admin
from .models import Room


admin.site.site_header = "Book It"
admin.site.register(Room)
