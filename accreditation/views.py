from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'current_page': request.path,
    }
    return render(request, 'accreditation/index.html', context)
