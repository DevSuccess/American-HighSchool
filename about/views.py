from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    aboutes = models.Info.objects.all()
    context = {
        'current_page': request.path,
        'aboutes': aboutes
    }
    return render(request, 'about/index.html', context)
