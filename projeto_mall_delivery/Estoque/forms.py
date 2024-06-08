from django import forms
from Estoque.models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Categoria', 'nome_item','quantidade']