from django.contrib import admin
from .models import Accreditation, List


class ListInline(admin.TabularInline):
    model = Accreditation.lists.through
    extra = 1


@admin.register(List)
class ListModelAdmin(admin.ModelAdmin):
    list_filter = ['type']
    list_display = ['name', 'type', 'date', 'description', 'admin_photo', 'created_at', 'updated_at']
    filter = ['name', 'image', 'type', 'date', 'description', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Accreditation)
class AccreditationModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    filter = ['title', 'description']
    inlines = [ListInline]
