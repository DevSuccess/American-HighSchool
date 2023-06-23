from django.shortcuts import render
from .models import Hour


# Create your views here.
def base_context(request):
    hours = Hour.get_current_hours()

    context = {
        'hours_now': hours
    }
    return context


def index(request):
    current_hours = Hour.get_current_hours()
    hours = Hour.objects.all()

    context = {
        'current_page': request.path,
        'current_hours': current_hours,
        'hours': hours
    }

    return render(request, 'hour/index.html', context)
