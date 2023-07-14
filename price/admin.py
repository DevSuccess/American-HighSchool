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
        'value', 'promotion', 'registration', 'birth', 'levels', 'formatted_price', 'formatted_registration')
    list_filter = ('levels',)
    search_fields = ('value', 'promotion', 'registration', 'birth', 'levels__name')
    fields = ('value', 'promotion', 'registration', 'birth', 'levels', 'formatted_price', 'formatted_registration')
    readonly_fields = ('formatted_price', 'formatted_registration')

    def save_model(self, request, obj, form, change):
        obj.calculate_price_promo()
        super().save_model(request, obj, form, change)
