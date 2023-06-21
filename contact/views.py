from django.shortcuts import render
from address.models import AddressAHSM
from contact.models import ContactHelp
from django.views import View
import random
from . import models


# Create your views here.
def base_context(request):
    # contacts_us = models.ContactUs.objects.all()
    contacts_helps = models.ContactHelp.objects.all()
    socials = models.Social.objects.all()

    # Liste pour stocker les numéros de téléphone
    phone_numbers = []

    # Parcourir les objets Info et obtenir les numéros de téléphone associés

    phone_numbers.extend([phone.number for phone in contacts_helps])

    # Sélectionner un numéro aléatoire parmi les numéros disponibles
    number_info = random.choice(phone_numbers) if phone_numbers else ""

    context = {
        # 'contacts_us': contacts_us,
        'contacts_helps': contacts_helps,
        'number_info': number_info,
        'socials': socials
    }
    return context


class ContactView(View):
    def get(self, request):
        # addresses = AddressAHSM.objects.all()
        # infos = ContactHelp.objects.all()
        # # Liste pour stocker les numéros de téléphone
        # phone_numbers = []
        # email = ''
        #
        # # Parcourir les objets Info et obtenir les numéros de téléphone associés
        # for info in infos:
        #     phone_numbers.extend([phone.number for phone in info.phones.all()])
        #     email = info.email
        #
        # # Sélectionner un numéro aléatoire parmi les numéros disponibles
        # number_info = random.choice(phone_numbers) if phone_numbers else ""

        # return render(request, 'contact/index.html', locals())
        return render(request, 'contact/index.html')
