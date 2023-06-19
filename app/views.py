from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
class HomeView(View):
    @staticmethod
    def get(request):
        addresses = models.Address.objects.all()
        contacts = models.Contact.objects.all()
        hours = models.Hour.get_current_hours()
        socials = models.Social.objects.all()
        movies = models.PresentationVideo.objects.latest('created_at')
        pictures = models.PresentationImage.objects.all()
        try:
            abouts = models.About.objects.latest('created_at')
        except models.About.DoesNotExist:
            abouts = None
        return render(request, 'home/index.html', locals())
