from django.contrib import admin
from .models import List, Accreditation


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date', 'admin_photo', 'created_at', 'updated_at')
    list_filter = ('type', 'date')
    search_fields = ('name', 'description')
    fields = ('name', 'type', 'date', 'description', 'image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'admin_lists')
    filter_horizontal = ('lists',)
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'lists')

    def admin_lists(self, obj):
        return ", ".join([str(list_obj) for list_obj in obj.lists.all()])
    admin_lists.short_description = 'Lists'
