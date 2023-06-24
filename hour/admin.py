from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Hour)
class HourModelAdmin(admin.ModelAdmin):
    list_display = ['day', 'open', 'close', 'message']
    fields = ['day', ('open', 'close'), 'message']
