from django.contrib import admin
from .models import PageGarde, PresentationVideo, PresentationImage, Activity, Membership

admin.site.site_header = 'Site Administration de AHS'
admin.site.site_title = "Page d'adminstation de AHS"
admin.site.index_title = "Manager"


@admin.register(PageGarde)
class PageGardeAdmin(admin.ModelAdmin):
    list_display = ('title', 'key', 'libel', 'admin_photo', 'created_at', 'updated_at')
    search_fields = ('title', 'key', 'libel')
    fields = ('title', 'key', 'libel', 'content', 'image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(PresentationVideo)
class PresentationVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'admin_video', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'video', 'admin_video', 'created_at', 'updated_at')
    readonly_fields = ('admin_video', 'created_at', 'updated_at')


@admin.register(PresentationImage)
class PresentationImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'admin_photo', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'image', 'admin_photo', 'created_at', 'updated_at')
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_photo', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title', 'image', 'admin_photo', 'created_at', 'updated_at')
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_photo', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title', 'image', 'admin_photo', 'created_at', 'updated_at')
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')
