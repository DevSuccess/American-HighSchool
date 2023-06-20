from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    try:
        abouts = models.About.objects.latest('created_at')
    except models.About.DoesNotExist:
        abouts = None

    context = {
        'abouts': abouts
    }
    return render(request, 'about/index.html', context)
