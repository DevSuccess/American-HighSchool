from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from accreditation import models as mdl
from . import models


# Create your views here.
class HomeView(View):
    def get(self, request):
        try:
            movies = models.PresentationVideo.objects.latest('created_at')
        except ObjectDoesNotExist:
            movies = None
        activities = models.Activity.objects.all()
        pictures = models.PresentationImage.objects.all()
        try:
            page_gardes = models.PageGarde.objects.latest('created_at')
        except ObjectDoesNotExist:
            page_gardes =  None
        try:
            memberships = models.Membership.objects.latest('created_at')
        except ObjectDoesNotExist:
            memberships = None

        lists = mdl.List.objects.all()
        context = {
            'current_page': request.path,
            'movies': movies,
            'pictures': pictures,
            'page_gardes': page_gardes,
            'activities': activities,
            'memberships': memberships,
            'lists': lists
        }
        return render(request, 'home/index.html', context)
