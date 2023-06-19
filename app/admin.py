from django.contrib import admin
from . import models


@admin.register(models.AboutList)
class AboutListModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    fields = ['name', 'status']


@admin.register(models.Activity)
class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'admin_photo']
    fields = [('title', 'active'), 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['lot', 'street', 'admin_map']
    fields = [('lot', 'street'), 'city', 'active', 'state', 'map', 'zip_code', 'created_at', 'updated_at']
    list_display_links = ['lot', 'street']
    readonly_fields = ['created_at', 'updated_at']

    def admin_map(self, obj):
        return obj.admin_map()

    admin_map.short_description = 'Map'


@admin.register(models.Collaborator)
class CollaboratorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'admin_photo']
    fields = ['name', 'date', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['contact', 'type']
    fields = ['contact', 'type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Hour)
class HourModelAdmin(admin.ModelAdmin):
    list_display = ['day', 'open', 'close', 'active', 'message']
    fields = ['day', ('open', 'close'), 'active', 'message']


@admin.register(models.Possibility)
class PossibilityModelAdmin(admin.ModelAdmin):
    list_display = ['value', 'active']
    fields = ['value', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Query)
class QueryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    fields = ['name', 'email', 'subject', 'message']


@admin.register(models.ServiceType)
class ServiceTypeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'admin_photo']
    fields = ['name', 'description', 'image', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'key', 'label', 'info_line', 'active']
    fields = ['title', 'label', 'key', 'info_line', 'all_service',  'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Social)
class SocialModelAdmin(admin.ModelAdmin):
    list_display = ['network_name', 'social_type', 'active', 'url']
    fields = ['network_name', 'social_type', 'url', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'start', 'occupation', 'admin_photo']
    fields = ['name', 'content', 'start', 'occupation', 'image', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Value)
class ValueModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'admin_photo']
    fields = ['content', 'image', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Vision)
class VisionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'admin_photo']
    fields = ['title', 'content', 'image', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Price)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['academic', 'price', 'registration', 'promotion', 'birth']
    fields = ['academic', 'price', 'registration', 'promotion', 'birth', 'possibilities']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Members)
class MembersModelAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'occupation', 'category', 'email', 'admin_photo', 'created_at', 'updated_at']
    fields = ['lastname', 'firstname', 'image', ('occupation', 'category'), 'email', 'contacts', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Accreditation)
class AccreditationModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'admin_photo']
    fields = ['content', 'collaborators', 'image']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'key', 'libel', 'content', 'admin_photo', 'created_at', 'updated_at']
    fields = ['title', 'key', 'libel', 'lists', 'content', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.PresentationVideo)
class PresentationVideoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'admin_video', 'created_at', 'updated_at']
    fields = ['title', 'active', 'description', 'video', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.PresentationImage)
class PresentationImageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'admin_photo', 'created_at', 'updated_at']
    fields = ['title', 'description', 'active', 'image', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
