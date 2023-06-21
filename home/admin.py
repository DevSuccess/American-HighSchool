from django.contrib import admin
from . import models


@admin.register(models.Possibility)
class PossibilityModelAdmin(admin.ModelAdmin):
    list_display = ['value', 'active', 'created_at', 'updated_at']
    fields = ['value', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


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