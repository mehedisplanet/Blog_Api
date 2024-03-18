from django.contrib import admin
from . import models
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['user','topic', 'title', 'body']

admin.site.register(models.Blog,BlogAdmin)
admin.site.register(models.Review)