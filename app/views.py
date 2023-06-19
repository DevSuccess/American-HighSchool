from django.shortcuts import render
from django.views import View
import random
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
        services = models.Service.objects.all()

        # Obtenir les membres dans un ordre aléatoire par catégorie
        members_direction = models.Members.objects.filter(category='A').order_by('?')
        members_administration = models.Members.objects.filter(category='B').order_by('?')
        members_enseignants = models.Members.objects.filter(category='C').order_by('?')

        return render(request, 'home/index.html', locals())
