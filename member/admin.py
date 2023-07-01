from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Member)
class MembersModelAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'occupation', 'category', 'admin_photo', 'created_at',
                    'updated_at']
    fields = ['lastname', 'firstname', 'image', ('occupation', 'category'), 'created_at',
              'updated_at']
    readonly_fields = ['created_at', 'updated_at']