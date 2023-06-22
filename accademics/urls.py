from django.urls import path

from . import views

app_name = 'accademics'
urlpatterns = [
    path('', views.index, name='index'),
]
