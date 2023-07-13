from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from . import models


# Create your views here.
class HomeView(View):
    def get(self, request):
        try:
            movies = models.PresentationVideo.objects.latest('created_at')
        except ObjectDoesNotExist:
            movies = None
        activities = models.Activity.objects.all()
        pictures = models.PresentationImage.objects.all()
        context = {
            'current_page': request.path,
            'movies': movies,
            'pictures': pictures,
            'activities': activities
        }
        return render(request, 'home/index.html', context)
