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


@admin.register(models.Accreditation)
class AccreditationModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'active', 'admin_photo']
    fields = ['content', 'collaborators', 'active', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Collaborator)
class CollaboratorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'active', 'admin_photo']
    fields = ['name', 'date', 'active', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

