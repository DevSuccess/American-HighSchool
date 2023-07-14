from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'category', 'occupation', 'admin_photo', 'created_at', 'updated_at')
    search_fields = ('lastname', 'firstname', 'category', 'occupation')
    list_filter = ('category',)
    fields = ('lastname', 'firstname', 'category', 'occupation', 'image', 'admin_photo', 'created_at', 'updated_at')
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')
