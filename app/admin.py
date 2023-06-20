from django.contrib import admin
from . import models


@admin.register(models.Level)
class LevelModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'admin_photo', 'created_at', 'updated_at']
    fields = ['name', 'status', 'image', 'prices', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


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
    list_display = ['number', 'active', 'created_at', 'updated_at']
    fields = ['number', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Hour)
class HourModelAdmin(admin.ModelAdmin):
    list_display = ['day', 'open', 'close', 'message']
    fields = ['day', ('open', 'close'), 'message']


@admin.register(models.Possibility)
class PossibilityModelAdmin(admin.ModelAdmin):
    list_display = ['value', 'active', 'created_at', 'updated_at']
    fields = ['value', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Query)
class QueryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'updated_at']
    fields = ['name', 'email', 'subject', 'message', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'admin_photo', 'active']
    fields = ['name', 'description', 'image', 'active', 'created_at', 'updated_at']
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


@admin.register(models.Vision)
class VisionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'admin_photo']
    fields = ['title', 'content', 'image', 'active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Price)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['price', 'registration', 'promotion', 'price_promo', 'birth']
    fields = ['price', 'registration', 'promotion', 'price_promo', 'birth', 'created_at', 'updated_at']
    readonly_fields = ['price_promo', 'created_at', 'updated_at']


@admin.register(models.Members)
class MembersModelAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'occupation', 'category', 'email', 'admin_photo', 'created_at',
                    'updated_at']
    fields = ['lastname', 'firstname', 'image', ('occupation', 'category'), 'email', 'contacts', 'created_at',
              'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Accreditation)
class AccreditationModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'admin_photo']
    fields = ['content', 'collaborators', 'image']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'key', 'libel', 'content', 'admin_photo', 'created_at', 'updated_at']
    fields = ['title', 'key', 'libel', 'content', 'image', 'created_at', 'updated_at']
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


@admin.register(models.Info)
class InfoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'active']
    fields = ['title', ('phones', 'email'), 'socials', 'active', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
