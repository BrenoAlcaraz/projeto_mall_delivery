from django.urls import path
from . import views

app_name = 'app_cadastro'

urlpatterns = [
    path('cadastro/cadastroconsumidor/', views.consumidor_cadastro, name='consumidor_cadastro'),
    path('cadastro/cadastrolojista/', views.lojista_cadastro, name='lojista_cadastro'),
    path('login/', views.pagina_login, name='pagina_login'),
    ##path('', views.pagina_inicial, name='pagina_inicial'),
    path('cadastro/lojista_inicial/',views.lojista_inicial,name='lojista_inicial')
]
