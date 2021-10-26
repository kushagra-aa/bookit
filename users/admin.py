from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(admin.ModelAdmin):

    fields = ('name', 'email', 'is_seller', 'contact')
    list_display = ('name', 'is_seller')
    list_filter = ('is_seller',)


admin.site.register(MyUser, UserAdminConfig)
