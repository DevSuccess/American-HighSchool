from django.contrib import admin
from . import models

admin.site\
    .site_header = "Admin American High School"
admin.site.site_title = "American High School"
admin.site.index_title = "Manageur"
admin.site.site_url =""


# Register your models here.
@admin.register(models.About)
class AboutModelAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ['title', 'libel', 'admin_photo', 'active', 'content']
    list_display_links = ['title', 'libel']
    fields = [('title', 'libel', 'active'), 'image', 'content', 'lists']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.AboutList)
class AboutModelAdmin(admin.ModelAdmin):
    fields = ['title', 'status']
    list_display = ['title', 'status']
