from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Vision)
class VisionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'active', 'admin_photo']
    fields = ['title', 'content', 'image', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
