from django.contrib import admin
from . import models

admin.site.site_header = 'Site Administration de AHS'
admin.site.site_title = "Page d'adminstation de AHS"
admin.site.index_title = "Manager"


@admin.register(models.PresentationVideo)
class PresentationVideoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'admin_video', 'created_at', 'updated_at']
    fields = ['title', 'active', 'description', 'video', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.PresentationImage)
class PresentationImageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'admin_photo', 'created_at', 'updated_at']
    fields = ['title', 'description', 'active', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Activity)
class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'description', 'admin_photo']
    fields = [('title', 'active'), 'description', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
