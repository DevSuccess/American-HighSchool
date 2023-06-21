# from about.models import *
# from activity.models import *
# from address.models import *
# from contact.models import *
# from home.models import *
# from hour.models import *
# from member.models import *
# from price.models import *
# from service.models import *
# from testimonie.models import *
# from vision.models import *
#
# import random
#
#
# def information(request):
#     addresses = AddressAHSM.objects.all()
#     contacts_us = ContactUs.objects.all()
#     our_contacts = ContactHelp.objects.all()
#     hours_now = Hour.get_current_hours()
#     socials = Social.objects.all()
#
#     services = Service.objects.all()
#
#     hour_lists = Hour.objects.all()
#     prices = Price.objects.all()
#     testimonials = Testimonial.objects.all()
#
#
#     # Sélectionner un numéro aléatoire parmi les numéros disponibles
#     number_info = random.choice(phone_numbers) if phone_numbers else ""
