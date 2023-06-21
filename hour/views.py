from django.shortcuts import render
from . import models


# Create your views here.
def base_context(request):
    hours = models.Hour.get_current_hours()

    context = {
        'hours_now': hours
    }
    return context


def index(request):
    pass
