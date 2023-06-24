from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'start', 'occupation', 'admin_photo']
    fields = ['name', 'content', 'start', 'occupation', 'contacts', 'image', 'active']
    readonly_fields = ['created_at', 'updated_at']
