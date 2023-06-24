from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.AboutAHSM)
class AboutAHSMModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'key', 'libel', 'content', 'admin_photo', 'created_at', 'updated_at']
    fields = ['title', 'key', 'libel', 'content', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.AboutHelp)
class AboutHelpModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'created_at', 'updated_at']
    fields = ['title', 'email', 'contacts', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.AboutITTI)
class AboutITTIModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'libel', 'description']
    fields = ['title', 'libel','description', 'type']
