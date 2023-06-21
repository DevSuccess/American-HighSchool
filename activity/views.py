from django.shortcuts import render
from . import models


# Create your views here.
def base_context(request):
    activitie_home = models.Activity.objects.all()

    context = {
        'activitie_home': activitie_home
    }
    return context


def index(request):
    pass
