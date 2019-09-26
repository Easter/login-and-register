from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import User,ConfirmString

class UserAdmin(ModelAdmin):
    list_display = ['name','password','email']

admin.site.register(User,UserAdmin)

admin.site.register(ConfirmString)
