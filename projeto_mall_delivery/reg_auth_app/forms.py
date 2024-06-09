from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Consumidor, Lojista
from django.contrib.auth.forms import AuthenticationForm


#Form Cadastro
class CreateConsumidorForm(forms.ModelForm):

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

#Form Cadastro
class CreateLojistaForm(forms.ModelForm):

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


#Form login
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



