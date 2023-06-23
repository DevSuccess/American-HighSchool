from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='index'),
]
