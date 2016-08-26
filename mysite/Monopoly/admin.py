#coding:utf8


# Register your models here.
from django.contrib import admin
from .models import users,chatcontent,buyshares
 
 
admin.site.register(users)
admin.site.register(chatcontent)
admin.site.register(buyshares)