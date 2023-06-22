from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='index'),
    path('<slug:slug>/', views.post_detail, name='detail'),
]
