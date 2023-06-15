from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Contact)
class ClassModelAdmin(admin.ModelAdmin):
    list_display = ['contact', 'contact_type', 'active', 'created_at', 'updated_at']
    list_editable = ['contact_type']
    filter = ['created_at', 'updated_at', 'active']
    fields = ['contact','contact_type', 'active']


@admin.register(models.Information)
class InformationModelAdmin(admin.ModelAdmin):
    list_display = ['localisation', 'day_begin', 'day_end', 'time_begin', 'time_end']
    fields = ['localisation', 'day_begin', 'day_end', 'time_begin', 'time_end', 'contacts', 'socials']
    list_editable = ['day_begin', 'day_end', 'time_begin', 'time_end']


@admin.register(models.Social)
class SocialModelAdmin(admin.ModelAdmin):
    list_display = ['network_name', 'social_type', 'url', 'active', 'created_at', 'updated_at']
    fields = ['network_name', 'social_type', 'url', 'active']
