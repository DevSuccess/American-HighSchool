from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'current_page': request.path,
        'queryset': queryset
    }
    return render(request, 'blog/index.html', context)