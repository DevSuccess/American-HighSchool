from django.contrib import admin
from . import models

admin.site.site_header = "Admin American High School"
admin.site.site_title = "American High School"
admin.site.index_title = "Manageur"


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']


# Register your models here.
@admin.register(models.About)
class AboutModelAdmin(BaseModelAdmin):
    list_display = ['title', 'libel', 'admin_photo', 'active', 'content']
    list_display_links = ['title', 'libel']
    fields = [('title', 'libel', 'active'), 'image', 'content', 'lists']


@admin.register(models.AboutList)
class AboutListModelAdmin(admin.ModelAdmin):
    fields = ['name', 'status']
    list_display = ['name', 'status']
