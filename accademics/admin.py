from django.contrib import admin
from .models import Academic


@admin.register(Academic)
class AcademicAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at')
    search_fields = ('value', 'description')
    fields = ('value', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
