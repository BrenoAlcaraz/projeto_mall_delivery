from django.shortcuts import render, redirect

from .models import *
from .forms import StockCreateForm,StockSearchForm,StockUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here
@login_required
def estoque(request):
    title="Welcome: This is the estoque page"   
    context = {
        "title" : title,
    }
    return render(request, 'estoque/estoque_home.html', context)

def lista_itens(request):
    title="Lista de Itens"   
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "title" : title,
        "queryset" : queryset,
        "form" : form,
    }
    if request.method == 'POST':
        queryset = Stock.objects.filter(Categoria__icontains = form['Categoria'].value(), nome_item__icontains=form['nome_item'].value())
        context = {
            "form":form,
            "title":title,
            "queryset": queryset,
    }

    return render(request, 'estoque/lista_itens.html', context)

def adicionar_itens(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_itens')
    context = {
        "form" : form,
        "title" : "Adicionar item",
    }
    return render(request,"estoque/adicionar_itens.html",context)

def update_itens(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_itens')
    context = {
        "form": form,
    }
    return render(request,"estoque/adicionar_itens.html",context)


def deletar_itens(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_itens')
    return render(request,'estoque/deletar_itens.html')

#view exibe estoque:
def sua_loja(request):
    stock = Stock.objects.all()
    
    query = request.GET.get('q', '')

    feed_data = []

    if query:
        produtos = Stock.objects.filter(nome__icontains=query)
    else:
        produtos = Stock.objects.all()

    return render(request, 'estoque/sua_loja.html')

    