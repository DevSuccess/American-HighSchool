from about.models import *
from contact.models import *
from home.models import *
from member.models import *
from service.models import *

import random


def information(request):
    addresses = Address.objects.all()
    contacts_us = ContactUs.objects.all()
    our_contacts = OurContact.objects.all()
    hours_now = Hour.get_current_hours()
    socials = Social.objects.all()

    try:
        abouts = About.objects.latest('created_at')
    except About.DoesNotExist:
        abouts = None

    services = Service.objects.all()

    hour_lists = Hour.objects.all()
    prices = Price.objects.all()
    testimonials = Testimonial.objects.all()
    infos = Info.objects.all()

    # Liste pour stocker les numéros de téléphone
    phone_numbers = []

    # Parcourir les objets Info et obtenir les numéros de téléphone associés
    for info in infos:
        phone_numbers.extend([phone.number for phone in info.phones.all()])

    # Sélectionner un numéro aléatoire parmi les numéros disponibles
    number_info = random.choice(phone_numbers) if phone_numbers else ""
