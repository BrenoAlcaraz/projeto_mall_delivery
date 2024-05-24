from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
]
