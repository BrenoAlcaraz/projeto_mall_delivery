from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:pk>/', views.detalhes_cliente, name='detalhes_cliente'),
    path('cliente/novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('cliente/deletar/<int:pk>/', views.deletar_cliente, name='deletar_cliente'),
]
