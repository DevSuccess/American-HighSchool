from django.shortcuts import render
from . import models


# Create your views here.
def base_context(request):
    try:
        abouts = models.AboutAHSM.objects.latest('created_at')
    except models.AboutAHSM.DoesNotExist:
        abouts = None

    context = {
        'about_home': abouts
    }

    return context


def index(request):
    mission = models.About.objects.filter(type='A')
    vision = models.About.objects.filter(type='B')
    context = {
        'current_page': request.path,
        'mission': mission,
        'vision': vision
    }
    return render(request, 'about/index.html', context)
