from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    try:
        members_direction = Members.objects.filter(category='A').order_by('?')
    except Members.DoesNotExist:
        members_direction = None

    try:
        members_administration = Members.objects.filter(category='B').order_by('?')
    except Members.DoesNotExist:
        members_administration = None

    try:
        members_enseignants = Members.objects.filter(category='C').order_by('?')
    except Members.DoesNotExist:
        members_enseignants = None
