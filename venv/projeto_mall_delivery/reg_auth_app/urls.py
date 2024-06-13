from django.urls import path, include
from .views import homepage, cadastro_lojista, user_login, escolha_user, UserLoginAPIView

app_name = 'app'

urlpatterns = [
    path('', homepage, name='homepage'),
    #path('cadastro_consumidor/', cadastro_consumidor, name='cadastro_consumidor'),
    path('cadastro_lojista/', cadastro_lojista, name='cadastro_lojista'),
    path('login/', user_login, name='login'),
    path('escolha_user/', escolha_user, name='escolha_user'),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
]
