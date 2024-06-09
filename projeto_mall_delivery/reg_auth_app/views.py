from django.shortcuts import render, redirect
from . forms import CreateConsumidorForm,CreateLojistaForm, LoginForm
from django.contrib.auth.models import auth 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import login as auth_login
#fç pagina principal
def homepage(request):
    return render(request,'app/index.html')

#fç de registro consumidor
def cadastro_consumidor(request):

    form = CreateConsumidorForm()

    if request.method == 'POST':
        form = CreateConsumidorForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('app:login')
        

    context = {'form_cadastro_consumidor':form}

    return render(request,'app/cadastro_consumidor.html',context=context)

#fç de registro lojista
def cadastro_lojista(request):

    form = CreateLojistaForm()

    if request.method == 'POST':
        form = CreateLojistaForm(request.POST or None)

        if form.is_valid():

            form.save()

            return redirect('app:login')

    context = {'form_cadastro_lojista':form}

    return render(request,'app/cadastro_lojista.html',context=context)

#fç pagina de login

def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("app:escolha_user")


    context = {'loginform':form}

    return render(request, 'app/login.html', context=context)


#fç pagina de escolha de usuario
def escolha_user(request):
    return render(request,'app/escolha_user.html')
