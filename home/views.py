from django.shortcuts import render
from django.views import View
import random
from django.core.exceptions import ObjectDoesNotExist
from . import models


# Create your views here.
class HomeView(View):
    def get(self, request):
        try:
            movies = models.PresentationVideo.objects.latest('created_at')
        except ObjectDoesNotExist:
            movies = None

        pictures = models.PresentationImage.objects.all()

        return render(request, 'home/index.html', locals())
