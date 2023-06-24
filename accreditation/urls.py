from django.urls import path
from . import views

app_name = 'accreditation'
urlpatterns = [
    path('', views.index, name='index')
]
