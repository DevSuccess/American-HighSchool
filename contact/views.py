from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
import random
from . import forms
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
        form = forms.ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact/index.html', context)

    def post(self, request):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            contacts = models.ContactUs(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            contacts.save()
            messages.success(request, "Congratulations ! Contact Send Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('home:index')
