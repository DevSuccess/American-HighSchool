from django.shortcuts import render
from django.views import View
import random
from django.core.exceptions import ObjectDoesNotExist
from . import models


# Create your views here.
class HomeView(View):

    def get(self, request):
        addresses = models.Address.objects.all()
        contacts = models.Contact.objects.all()
        hours = models.Hour.get_current_hours()
        socials = models.Social.objects.all()

        try:
            movies = models.PresentationVideo.objects.latest('created_at')
        except ObjectDoesNotExist:
            movies = None

        pictures = models.PresentationImage.objects.all()

        try:
            abouts = models.About.objects.latest('created_at')
        except models.About.DoesNotExist:
            abouts = None

        services = models.Service.objects.all()

        try:
            members_direction = models.Members.objects.filter(category='A').order_by('?')
        except models.Members.DoesNotExist:
            members_direction = None

        try:
            members_administration = models.Members.objects.filter(category='B').order_by('?')
        except models.Members.DoesNotExist:
            members_administration = None

        try:
            members_enseignants = models.Members.objects.filter(category='C').order_by('?')
        except models.Members.DoesNotExist:
            members_enseignants = None

        hour_lists = models.Hour.objects.all()
        prices = models.Price.objects.all()
        testimonials = models.Testimonial.objects.all()
        infos = models.Info.objects.all()

        # Liste pour stocker les numéros de téléphone
        phone_numbers = []

        # Parcourir les objets Info et obtenir les numéros de téléphone associés
        for info in infos:
            phone_numbers.extend([phone.number for phone in info.phones.all()])

        # Sélectionner un numéro aléatoire parmi les numéros disponibles
        number_info = random.choice(phone_numbers) if phone_numbers else ""

        return render(request, 'home/index.html', locals())
