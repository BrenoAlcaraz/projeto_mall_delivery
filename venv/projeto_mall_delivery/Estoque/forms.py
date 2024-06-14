from django import forms
from Estoque.models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Categoria', 'nome_item', 'quantidade','Preço']

   

    def clean_nome_item(self):
        nome_item = self.cleaned_data.get('nome_item')
        if not nome_item:
            raise forms.ValidationError('Campo nome é obrigatório')
        for instance in Stock.objects.all():
            if instance.nome_item == nome_item:
                raise forms.ValidationError(nome_item + ' já existe')
        return nome_item

class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Categoria', 'nome_item','Preço']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Categoria', 'nome_item', 'quantidade','Preço']
