from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
class HomeView(View):
    def get(self, request):
        video = models.Video.objects.latest('updated_at')
        if not video.url and video.file:
            video_url = video.file
        else:
            video_url = video.url

        images = models.Image.objects.all()
        return render(request, 'home/index.html', locals())
