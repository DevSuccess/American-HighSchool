from django.contrib import admin
from .models import Support, Info


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'display_contacts')
    filter_horizontal = ('contacts',)
    search_fields = ('title', 'email')
    fields = ('title', 'email', 'contacts')

    def display_contacts(self, obj):
        return ', '.join(str(contact) for contact in obj.contacts.all())

    display_contacts.short_description = 'Contacts'


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_photo')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'image', 'admin_photo')
    readonly_fields = ('admin_photo',)
