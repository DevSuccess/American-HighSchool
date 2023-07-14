from django.contrib import admin
from .models import Support, Info


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')
    filter_horizontal = ('contacts',)
    fields = ('title', 'email', 'contacts')


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'admin_photo')
    list_filter = ('type',)
    search_fields = ('title', 'description')
    fields = ('title', 'libel', 'description', 'type', 'image')
