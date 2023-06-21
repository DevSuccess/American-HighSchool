from django.shortcuts import render
from .models import Member

def base_context(request):
    try:
        direction_home = Member.objects.filter(category='A').order_by('?')
    except Member.DoesNotExist:
        members_direction = None

    try:
        administration_home = Member.objects.filter(category='B').order_by('?')
    except Member.DoesNotExist:
        members_administration = None

    try:
        enseignants_home = Member.objects.filter(category='C').order_by('?')
    except Member.DoesNotExist:
        members_enseignants = None

    context = {
        'direction_home': direction_home,
        'administration_home': administration_home,
        'enseignants_home': enseignants_home
    }
    return context

def index(request):
    pass
