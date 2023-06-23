from django.shortcuts import render
from . import models


# Create your views here.
def base_context(request):
    prices = models.Price.objects.all()

    context = {
        'price_lists': prices
    }

    return context


def index(request):
    pass
