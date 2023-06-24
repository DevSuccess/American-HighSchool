from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Registration)
class RegisterModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'age', 'gender', 'message']
    fields = [('first_name', 'last_name'), ('email', 'phone'), 'age',
              'gender', 'address', ('city', 'zip_code'), 'country', 'message',
              'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
