from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.ContactHelp)
class ContactHelpModelAdmin(admin.ModelAdmin):
    list_display = ['number', 'active', 'created_at', 'updated_at']
    fields = ['number', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'active', 'message', 'created_at']
    fields = ['name', 'email', 'subject', 'active', 'message', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.ContactClient)
class ContactClientModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'active', 'created_at', 'updated_at']
    fields = ['email', 'phone', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Social)
class SocialModelAdmin(admin.ModelAdmin):
    list_display = ['network_name', 'social_type', 'url', 'active', 'created_at']
    fields = ['network_name', 'social_type', 'url', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
