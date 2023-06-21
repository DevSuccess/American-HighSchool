from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Price)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['price', 'registration', 'promotion', 'active', 'price_promo', 'admin_photo', 'birth']
    fields = ['price', 'registration', 'promotion', 'active', 'price_promo', ('birth', 'image'), 'created_at',
              'updated_at']
    readonly_fields = ['price_promo', 'created_at', 'updated_at']


@admin.register(models.Level)
class LevelModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'updated_at']
    fields = ['name', 'status', 'prices', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
