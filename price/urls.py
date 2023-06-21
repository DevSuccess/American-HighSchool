from django.urls import path

from . import views

app_name = 'price'
urlpatterns = [
    path('', views.index, name='index'),
]
