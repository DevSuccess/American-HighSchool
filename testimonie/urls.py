from django.urls import path

from . import views

app_name = 'testimonie'
urlpatterns = [
    path('', views.index, name='index'),
]
