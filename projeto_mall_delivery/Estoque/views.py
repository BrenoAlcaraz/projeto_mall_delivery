from django.shortcuts import render
from .models import *
from .forms import StockCreateForm
# Create your views here.
def estoque(request):
    title="Welcome: This is the estoque page"   
    context = {
        "title" : title,
    }
    return render(request, 'estoque/estoque_home.html', context)

def lista_itens(request):
    title="Lista de Itens"   
    queryset = Stock.objects.all()
    context = {
        "title" : title,
        "queryset" : queryset,
    }
    return render(request, 'estoque/lista_itens.html', context)

def adicionar_itens(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form,
        "title" : "Adicionar item",
    }
    return render(request,"estoque/adicionar_itens.html",context)
