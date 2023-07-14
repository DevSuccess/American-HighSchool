from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    mission = models.Info.objects.filter(type='A')
    vision = models.Info.objects.filter(type='B')
    organisation = models.Info.objects.filter(type='C')
    context = {
        'current_page': request.path,
        'mission': mission,
        'vision': vision,
        'organisation': organisation
    }
    return render(request, 'about/index.html', context)
