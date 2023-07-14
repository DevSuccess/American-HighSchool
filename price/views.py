from django.shortcuts import render
from . import models


# Create your views here.
def base_context(request):
    prices = models.Price.objects.all()
    levels = models.Level.objects.all()

    context = {
        'prices': prices,
        'levels': levels
    }

    return context
