from django.shortcuts import render
from .models import Member


# Create your views here.
def index(request):
    try:
        members_direction = Member.objects.filter(category='A').order_by('?')
    except Member.DoesNotExist:
        members_direction = None

    try:
        members_administration = Member.objects.filter(category='B').order_by('?')
    except Member.DoesNotExist:
        members_administration = None

    try:
        members_enseignants = Member.objects.filter(category='C').order_by('?')
    except Member.DoesNotExist:
        members_enseignants = None
