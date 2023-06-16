from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['contact', 'contact_type', 'active', 'created_at', 'updated_at']
    list_editable = ['contact_type']
    filter = ['created_at', 'updated_at', 'active']
    fields = ['contact', 'contact_type', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Information)
class InformationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'addresses', 'contacts', 'hours', 'socials']
    fields = ['name', 'addresses', 'contacts', 'hours', 'socials']


@admin.register(models.Social)
class SocialModelAdmin(admin.ModelAdmin):
    list_display = ['network_name', 'social_type', 'url', 'active', 'created_at', 'updated_at']
    fields = ['network_name', 'social_type', 'url', 'active']


@admin.register(models.Address)
class AddressModelAdmin(admin.ModelAdmin):
    fields = ['street', 'city', 'active', 'url', 'state', 'zip_code', ]
    list_display = ['street', 'city', 'active', 'url', 'state', 'zip_code', 'updated_at']


@admin.register(models.Hour)
class HourModelAdmin(admin.ModelAdmin):
    list_display_links = ['day']
    list_display = ['day', 'open', 'close', 'active', 'message']
    fields = ['day', 'open', 'close', 'active', 'message']
    list_editable = ['open', 'close']


@admin.register(models.About)
class AboutModelAdmin(admin.ModelAdmin):
    fields = ['title', 'libel', 'image', 'active', 'content', 'lists']
    list_display = ['title', 'libel', 'admin_photo', 'active', 'content']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.AboutList)
class AboutModelAdmin(admin.ModelAdmin):
    fields = ['title', 'status']
    list_display = ['title', 'status']
