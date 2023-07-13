from . import views
from django.urls import path

app_name = 'new'
urlpatterns = [
    path('', views.index, name='index'),
]
