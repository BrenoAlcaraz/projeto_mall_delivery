from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Lojista

#form de cadastro de lojista
class CreateLojistaForm(UserCreationForm):
    class Meta:
        model = Lojista
        fields = ['username', 'email', 'cpf', 'telefone', 'cep', 'endereco', 'cnpj', 'razao_social']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Insira seu nome de usuário' }),
            'email': forms.EmailInput(attrs={'placeholder': 'Insira seu e-mail'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Insira seu CPF'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Insira seu telefone'}),
            'cep': forms.TextInput(attrs={'placeholder': 'Insira o CEP da sua loja'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Insira o endereço da sua loja'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'Insira o CNPJ da sua loja'}),
            'razao_social': forms.TextInput(attrs={'placeholder': 'Insira a razão social da loja'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_approved = False  # Usuário não aprovado por padrão
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CreateLojistaForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'cpf','telefone','cep','endereco','cnpj','razao_social','password1','password2']:
            self.fields[fieldname].help_text = None

#form de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Nome de usuário'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Senha'}))

#uma das diferenças aqui é que o UserCreationForm trata as senhas de maneira mais segura, salvando apenas o hash no banco