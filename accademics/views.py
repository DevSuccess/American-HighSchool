from django.shortcuts import render
from .models import Academic


# Create your views here.
def index(request):
    accademics = Academic.objects.all()
    context = {
        'current_page': request.path,
        'accademics': accademics,
    }
    return render(request, 'accademics/index.html', context)
