from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'occupation')
    list_filter = ('start',)
    search_fields = ('name', 'occupation')
    fields = ('name', 'content', 'start', 'occupation', 'image', 'admin_photo', 'created_at', 'updated_at')
    readonly_fields = ('admin_photo', 'created_at', 'updated_at')
