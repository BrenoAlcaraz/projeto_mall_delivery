from django import forms
from Estoque.models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Categoria', 'nome_item','quantidade']

    def clean_Categoria(self):
        Categoria = self.cleaned_data.get('Categoria')
        if not Categoria:
            raise forms.ValidationError('Campo categoria é obrigatório')
        for instance in Stock.objects.all():
            if instance.Categoria == Categoria:
                raise forms.ValidationError(Categoria + ' já existe')
        return Categoria
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
        fields = ['Categoria','nome_item']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Categoria', 'nome_item', 'quantidade']