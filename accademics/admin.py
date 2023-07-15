from django.contrib import admin
from .models import Academic


@admin.register(Academic)
class AcademicAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at', 'updated_at')
    search_fields = ('value', 'description')
    list_filter = ('value',)

    fieldsets = (
        ('Academic Details', {
            'fields': ('value', 'description', 'created_at', 'updated_at'),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
