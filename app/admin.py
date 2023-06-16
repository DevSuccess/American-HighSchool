from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.About)
class AboutModelAdmin(admin.ModelAdmin):
    fields = ['title', 'libel', 'image', 'active', 'content', 'lists']
    list_display = ['title', 'libel', 'admin_photo', 'active', 'content']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.AboutList)
class AboutModelAdmin(admin.ModelAdmin):
    fields = ['title', 'status']
    list_display = ['title', 'status']
