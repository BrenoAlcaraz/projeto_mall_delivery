from django.shortcuts import render, redirect
from .forms import ConsumidorCadastroForm, LojistaCadastroForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def consumidor_cadastro(request):
    if request.method == 'POST':
        form = ConsumidorCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # substitua 'pagina_de_login' pela sua página de login
    else:
        form = ConsumidorCadastroForm()
    return render(request, 'cadastro_consumidor.html', {'form': form})

def lojista_cadastro(request):
    if request.method == 'POST':
        form = LojistaCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # substitua 'pagina_de_login' pela sua página de login
    else:
        form = LojistaCadastroForm()
    return render(request, 'cadastro_lojista.html', {'form': form})

def pagina_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('lojista_inicial.html')  # substitua 'pagina_inicial' pela página inicial do seu sistema
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    return render(request, 'login.html')

##def pagina_inicial(request):
   ## return render(request, 'pagina_inicial.html')

def login_view(request):
    # Sua lógica para a view de login aqui
    return render(request, 'login.html')

def lojista_inicial(request):
    return render(request,'lojista_inicial.html')
