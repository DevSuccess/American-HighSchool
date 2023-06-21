from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Activity)
class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'description', 'admin_photo']
    fields = [('title', 'active'), 'description', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
