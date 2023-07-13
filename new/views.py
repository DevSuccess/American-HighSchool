from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    news = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'news': news
    }
    return render(request, 'news/index.html', context)
