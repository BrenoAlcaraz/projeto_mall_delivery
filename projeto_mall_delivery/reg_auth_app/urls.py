from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('cadastro_consumidor/',views.cadastro_consumidor, name='cadastro_consumidor'),  
    path('cadastro_lojista/',views.cadastro_lojista, name='cadastro_lojista'), 
    path('login/',views.login, name='login'), 
    path('escolha_user/',views.escolha_user, name='escolha_user'), 
]