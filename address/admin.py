from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Localisation


@admin.register(Localisation)
class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'lot', 'state', 'zip_code', 'admin_map')
    list_filter = ('state',)
    search_fields = ('street', 'city', 'zip_code')
    fields = ('street', 'city', 'lot', 'state', 'zip_code', 'map', 'admin_map')
    readonly_fields = ('admin_map',)

    def admin_map(self, obj):
        return mark_safe(obj.map)
    admin_map.short_description = 'Map'
