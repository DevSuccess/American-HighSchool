from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    accreditations = models.Accreditation.objects.all()
    context = {
        'current_page': request.path,
        'accreditations': accreditations
    }
    return render(request, 'accreditation/index.html', context)
