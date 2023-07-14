from django.contrib import admin
from .models import Contact, Social, ContactUs


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('number',)
    fields = ('number',)
    search_fields = ('number',)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('network_name', 'social_type', 'url')
    fields = ('network_name', 'social_type', 'url')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    fields = ('name', 'email', 'subject', 'message', 'created_at', 'updated_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at', 'updated_at')
