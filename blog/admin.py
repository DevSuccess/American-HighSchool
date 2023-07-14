from django.contrib import admin
from .models import Post, Slogan


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'admin_photo', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ["title"]}
    fields = ('title', 'slug', 'author', 'content', 'status', 'image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Slogan)
class SloganAdmin(admin.ModelAdmin):
    list_display = ('title', 'note', 'admin_photo', 'created_at')
    search_fields = ('title', 'note')
    fields = ('title', 'note', 'description', 'image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
