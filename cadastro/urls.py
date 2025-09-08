from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaExterna, name='externa'),
    path('barbearia/', views.barbearia, name='barbearia'),
    path('sair/', views.sair, name='sair'),
]
