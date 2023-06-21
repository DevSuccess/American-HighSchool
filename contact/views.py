from django.shortcuts import render
from address.models import AddressAHSM
from contact.models import ContactHelp
from django.views import View
import random


# Create your views here.
class ContactView(View):
    def get(self, request):
        addresses = AddressAHSM.objects.all()
        infos = ContactHelp.objects.all()
        # Liste pour stocker les numéros de téléphone
        phone_numbers = []
        email = ''

        # Parcourir les objets Info et obtenir les numéros de téléphone associés
        for info in infos:
            phone_numbers.extend([phone.number for phone in info.phones.all()])
            email = info.email

        # Sélectionner un numéro aléatoire parmi les numéros disponibles
        number_info = random.choice(phone_numbers) if phone_numbers else ""

        return render(request, 'contact/index.html', locals())
