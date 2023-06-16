from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
class HomeView(View):
    def get(self, request):
        videos = models.Video.objects.all()
        latest_video = videos.latest('updated_at')
        print("Video : ", latest_video)
        if not latest_video.url and latest_video.file:
            video_url = latest_video.file.url
        else:
            video_url = latest_video.url
        video_title = latest_video.title
        video_description = latest_video.description
        images = models.Image.objects.all()
        context = {
            'video_title': video_title,
            'video_url': video_url,
            'video_description': video_description,
            'images': images
        }
        return render(request, 'home/index.html', context)

