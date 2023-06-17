from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
class HomeView(View):
    @staticmethod
    def get(request):
        addresses = models.Address.objects.all()

        return render(request, 'home/index.html', locals())
