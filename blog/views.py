from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'queryset': queryset
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    context = {
        'post': post
    }
    return render(request, 'blog/details.html', context)
