from django.shortcuts import render
from . import models


# Create your views here.
def base_context(request):
    testimonials = models.Testimonial.objects.all()

    context = {
        'testimonials_home': testimonials
    }

    return context


def index(request):
    pass
