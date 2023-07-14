from django.contrib import admin
from .models import Academic


@admin.register(Academic)
class AcademicAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_photo', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
