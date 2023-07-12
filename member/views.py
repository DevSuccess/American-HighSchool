from django.shortcuts import render
from .models import Member


# def base_context(request):
#     try:
#         # direction_home = Member.objects.filter(category='A').order_by('?')
#         direction_home = Member.objects.filter(category='A').first()
#     except Member.DoesNotExist:
#         direction_home = None
#
#     try:
#         administration_home = Member.objects.filter(category='B').order_by('?')
#     except Member.DoesNotExist:
#         administration_home = None
#
#     try:
#         enseignants_home = Member.objects.filter(category='C').order_by('?')
#     except Member.DoesNotExist:
#         enseignants_home = None
#
#     context = {
#         'current_page': request.path,
#         'direction_home': direction_home,
#         'administration_home': administration_home,
#         'enseignants_home': enseignants_home
#     }
#     return context

def base_context(request):
    try:
        members = Member.objects.latest('created_at')
    except Member.DoesNotExist:
        members = None

    context = {
        'members': members
    }
    return context


def index(request):
    members = Member.objects.all()
    context = {
        'current_page': request.path,
        'members': members
    }
    return render(request, 'member/index.html', context)
