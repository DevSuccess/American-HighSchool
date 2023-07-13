from django.contrib import admin
from .models import UserPost, Post


# Register your models here.
@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_photo')
    fields = ['name', 'image']
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_photo', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    fields = ['title', 'author', 'content', 'image', 'status', 'created_at', 'updated_at']
    search_fields = ('title',)
    # prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
