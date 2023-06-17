from django.contrib import admin
from . import models

admin.site.index_title = "Manageur"
admin.site.site_header = "Admin American High School"
admin.site.site_title = "American High School"


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.About)
class AboutModelAdmin(BaseModelAdmin):
    list_display = ['title', 'libel', 'active', 'admin_photo']
    list_display_links = ['title', 'libel']
    fields = [('title', 'active'), ('image', 'lists'), 'libel', 'content', 'created_at', 'updated_at']


@admin.register(models.AboutList)
class AboutListModelAdmin(admin.ModelAdmin):
    fields = ['name', 'status']
    list_display = ['name', 'status']
