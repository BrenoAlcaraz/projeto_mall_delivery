from django.urls import path
from . import views
urlpatterns = [
    path('',views.estoque, name='estoque_home'),
    path('lista_itens/', views.lista_itens, name='lista_itens'),
    path('adicionar_itens/', views.adicionar_itens, name='adicionar_itens'),
      path('update_itens/<str:pk>/', views.update_itens,name='update_itens'),

]