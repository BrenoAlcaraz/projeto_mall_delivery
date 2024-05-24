from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

@login_required
def lista_produtos(request):
    produtos = Produto.objects.filter(lojista=request.user)
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.lojista = request.user
            produto.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})