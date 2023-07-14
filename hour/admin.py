from django.contrib import admin
from .models import Hour


@admin.register(Hour)
class HourAdmin(admin.ModelAdmin):
    list_display = ('day', 'open', 'close', 'message')
    list_filter = ('day',)
    search_fields = ('day', 'open', 'close', 'message')
    fields = ('day', 'open', 'close', 'message')
