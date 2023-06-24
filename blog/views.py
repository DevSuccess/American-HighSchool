from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post, Slogan


def index(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    slogan = Slogan.objects.all().first()
    context = {
        'current_page': request.path,
        'queryset': queryset,
        'slogan': slogan
    }
    return render(request, 'blog/index.html', context)