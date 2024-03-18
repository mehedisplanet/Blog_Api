from django.contrib import admin
from . import models
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

admin.site.register(models.Contact_us,ContactAdmin)