from django.shortcuts import render
from . import models


# Create your views here.
def base_context(request):
    levels = models.Level.objects.all()

    context = {
        'level_lists': levels
    }

    return context


def index(request):
    pass
