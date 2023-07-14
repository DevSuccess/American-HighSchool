from django.contrib import admin
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'phone', 'age', 'gender', 'address', 'city', 'zip_code', 'country')
    list_filter = ('gender', 'country')
    search_fields = (
        'first_name', 'last_name', 'email', 'phone')
    fields = (
        'first_name', 'last_name', 'email', 'phone',
        'age', 'gender', 'address', 'city', 'zip_code', 'country', 'message')
    readonly_fields = ('created_at', 'updated_at')
