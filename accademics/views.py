from django.shortcuts import render
from .models import Accademics


# Create your views here.
def index(request):
    accademics = Accademics.objects.all()
    context = {
        'accademics': accademics,
    }
    return render(request, 'accademics/index.html', context)
