from django import forms
from .models import Consumidor, Lojista

class ConsumidorCadastroForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['username', 'email', 'password', 'cpf', 'telefone']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Insira seu nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Insira seu e-mail'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Insira sua senha'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Insira seu CPF'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Insira seu telefone'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''  # Remova o texto de ajuda para o campo1    

class LojistaCadastroForm(forms.ModelForm):
    class Meta:
        model = Lojista
        fields = ['username', 'email', 'password', 'cpf', 'cep', 'endereco', 'cnpj', 'razao_social']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Insira seu nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Insira seu e-mail'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Insira sua senha'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Insira seu CPF'}),
            'cep': forms.TextInput(attrs={'placeholder': 'Insira o CEP da sua loja'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Insira o endereço da sua loja'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'Insira o CNPJ da sua loja'}),
            'razao_social': forms.TextInput(attrs={'placeholder': 'Insira a razão social da loja'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''  # Remova o texto de ajuda para o campo1    
