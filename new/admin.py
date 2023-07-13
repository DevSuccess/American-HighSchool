from django.contrib import admin
from .models import UserPost, Post


# Register your models here.

@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    # search_fields = ('author__name', 'content')
    search_fields = ('content')
    date_hierarchy = 'created_on'
    readonly_fields = ('created_on', 'updated_on')

    fieldsets = (
        ('Post Details', {
            'fields': ('author', 'title', 'content', 'image')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_on', 'updated_on'),
            'classes': ('collapse',)
        })
    )
