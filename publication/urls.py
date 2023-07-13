from publication import views
from django.urls import path

app_name = 'publication'
urlpatterns = [
    path('', views.index, name='index'),
]
