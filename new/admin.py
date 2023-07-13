from django.contrib import admin
from .models import UserPost, Post

# Register your models here.
@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'author__name')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_on'
    ordering = ('-created_on',)
