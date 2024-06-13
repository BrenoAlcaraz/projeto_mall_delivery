from django.shortcuts import render, redirect
from .forms import CreateConsumidorForm, CreateLojistaForm, LoginForm
from django.contrib.auth import login as auth_login, authenticate
import logging 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserLoginSerializer

#página principal
def homepage(request):
    return render(request, 'app/index.html')

#registro de consumidor
def cadastro_consumidor(request):
    if request.method == 'POST':
        #se o método for POST, ele cria um formulário com os dados inseridos
        form = CreateConsumidorForm(request.POST)
        if form.is_valid():
            #se for válido, salva os dados e leva pra página de login
            form.save()
            return redirect('app:login')
    else:
        #se não for POST, cria um formulário vazio
        form = CreateConsumidorForm()
    
    #renderiza o cadastro com o form
    context = {'form_cadastro_consumidor': form}
    return render(request, 'app/cadastro_consumidor.html', context=context)

#registro de lojista
def cadastro_lojista(request):
    if request.method == 'POST':
        #mesma coisa do consumidor, se for POST, cria o form com os dados
        form = CreateLojistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = CreateLojistaForm()
    
    context = {'form_cadastro_lojista': form}
    return render(request, 'app/cadastro_lojista.html', context=context)

#isso esquece, fui tentar debbugar
logger = logging.getLogger(__name__)

# Página de Login
def user_login(request):
    logger.debug("Received login request")
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            #se o form for válido, extrai os dados do login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            logger.debug(f"Attempting to authenticate user: {username}")
            #tentativa de autenticar o usuário
            user = authenticate(request, username=username, password=password)
            if user is not None:
                logger.debug("User authentication successful")
                #se for tudo certo, redireciona pra escolha de usuário
                auth_login(request, user)
                return redirect("estoque_home")
            else:
                logger.debug("User authentication failed")

    #renderiza a página de login com usuário
    context = {'loginform': form}
    return render(request, 'app/login.html', context=context)

#API pra login
class UserLoginAPIView(APIView):
    def post(self, request):
        #cria o serializer
        serializer = UserLoginSerializer(data=request.data)
        #valida os dados do serializer
        serializer.is_valid(raise_exception=True)
        #se os dados estiverem certos, o user é autenticado
        user = serializer.validated_data['user']
        #gera o token pro usuario
        token, created = Token.objects.get_or_create(user=user)
        #retorna a resposta do token
        return Response({'token': token.key}, status=status.HTTP_200_OK)

#página de escolha do usuário
def escolha_user(request):
    return render(request, 'app/escolha_user.html')
