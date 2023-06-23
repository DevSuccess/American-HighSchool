from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Price)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['value', 'registration', 'promotion', 'active', 'price_promo', 'admin_photo', 'birth', 'get_level']
    fields = ['value', 'registration', 'promotion', 'levels', 'active', 'price_promo', ('birth', 'image'), 'created_at', 'updated_at']
    readonly_fields = ['price_promo', 'created_at', 'updated_at']

    def get_level(self, obj):
        if obj.levels is not None:
            return obj.levels.name
        return None

    get_level.short_description = 'Level'


@admin.register(models.Level)
class LevelModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'updated_at']
    fields = ['name', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
