from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Accademics)
class AccademicModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active', 'admin_photo']
    fields = ['name', 'description', 'image', 'type', 'active', 'created_at', 'updated_at']
    readonly_fields = ['updated_at', 'created_at']
