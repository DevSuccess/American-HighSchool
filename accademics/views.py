from django.shortcuts import render
from .models import Accademics


# Create your views here.
def index(request):
    try:
        section1 = Accademics.objects.filter(type='A')
    except Accademics.DoesNotExist:
        section1 = None

    try:
        section2 = Accademics.objects.filter(type='B')
    except Accademics.DoesNotExist:
        section2 = None

    try:
        section3 = Accademics.objects.filter(type='C')
    except Accademics.DoesNotExist:
        section3 = None
        
    context = {
        'current_page': request.path,
        'section1': section1,
        'section2': section2,
        'section3': section3
    }
    return render(request, 'accademics/index.html', context)
