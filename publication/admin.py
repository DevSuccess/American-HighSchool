from django.contrib import admin
from .models import Author, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_photo')
    search_fields = ('name',)
    fields = ('name', 'image', 'admin_photo')
    readonly_fields = ('admin_photo',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'admin_photo', 'created_at', 'updated_at')
    list_filter = ('author', 'status')
    search_fields = ('title', 'author__name')
    fields = ('title', 'author', 'content', 'status', 'image', 'admin_photo', 'created_at', 'updated_at')
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')
