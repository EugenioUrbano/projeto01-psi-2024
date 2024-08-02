from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('jogadores/', views.jogadores, name='jogadores'),
    path('sobre/', views.jogadores, name='sobre'),
]