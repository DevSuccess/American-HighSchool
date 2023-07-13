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
    list_display = ('title', 'admin_photo', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    fields = ['title', 'author', 'content', 'image', 'status', 'created_on', 'updated_on']
    search_fields = ('title',)
    # prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_on', 'updated_on']
    date_hierarchy = 'created_on'
    ordering = ('-created_on',)
