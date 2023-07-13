from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.AddressAHSM)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['lot', 'street', 'admin_map']
    fields = [('lot', 'street'), 'city', 'active', 'state', 'map', 'zip_code', 'created_at', 'updated_at']
    list_display_links = ['lot', 'street']
    readonly_fields = ['created_at', 'updated_at']

    def admin_map(self, obj):
        return obj.admin_map()

    admin_map.short_description = 'Map'