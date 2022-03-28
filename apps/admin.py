from django.contrib import admin
from . import models

class ContactAdmin(admin.ModelAdmin):
    list_display=['id', 'full_name', 'email', 'number', 'address']
admin.site.register(models.Contact,ContactAdmin)
