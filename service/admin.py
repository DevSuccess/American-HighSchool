from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active', 'admin_photo']
    fields = ['name', 'description', 'image', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
