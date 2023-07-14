from django.contrib import admin
from .models import Level, Price


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    fields = ('name', 'status')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'value', 'promotion', 'registration', 'admin_photo', 'birth', 'levels', 'formatted_value', 'formatted_value')
    list_filter = ('levels',)
    search_fields = ('value', 'promotion', 'registration', 'birth', 'levels__name')
    fields = (
        'value', 'promotion', ('image',), 'admin_photo', 'registration',
        'birth', 'levels', 'formatted_value', 'formatted_registration')
    readonly_fields = ('admin_photo', 'formatted_value', 'formatted_registration')
