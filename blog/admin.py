from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'content', 'status', 'created_on', 'updated_on')
    fields = ['title', 'slug', 'author', 'content', 'status', 'image', 'created_on', 'updated_on']
    readonly_fields = ['created_on', 'updated_on']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Slogan)
class SloganModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'admin_photo', 'created_at', 'updated_at')
    fields = ['title', 'description', 'note', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
