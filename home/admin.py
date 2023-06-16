from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Video)
class VideoModelAdmin(admin.ModelAdmin):
    search_fields = ['title']
    fields = ['title', 'url', 'active', 'description', 'file', 'created_at', 'updated_at']
    list_display = ['title', 'active', 'admin_video', 'description', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

