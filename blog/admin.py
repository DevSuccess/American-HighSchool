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
