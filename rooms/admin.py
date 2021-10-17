from django.contrib import admin
from .models import room
# Register your models here.
admin.site.site_header = "Book It"
admin.site.register(room)
