from django.contrib import admin
from  Estoque.models import Stock,Categoria
from Estoque.forms import StockCreateForm

# Register your models here.
class StockCreateadmin(admin.ModelAdmin):
    list_display = ['Categoria', 'nome_item', 'quantidade']
    form = StockCreateForm
    list_filter = ['Categoria']
    search_fields = ['Categoria','nome_item']




admin.site.register(Stock, StockCreateadmin)
admin.site.register(Categoria)