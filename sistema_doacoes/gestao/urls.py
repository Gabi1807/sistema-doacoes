from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/doador/', views.cadastrar_doador, name='cadastrar_doador'),
    path('cadastrar/beneficiario/', views.cadastrar_beneficiario, name='cadastrar_beneficiario'),
    path('cadastrar/item/', views.cadastrar_item, name='cadastrar_item'),
    path('cadastrar/doacao/', views.cadastrar_doacao, name='cadastrar_doacao'),
]