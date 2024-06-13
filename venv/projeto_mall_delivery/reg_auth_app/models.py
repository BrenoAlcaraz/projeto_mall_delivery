from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _

class Lojista(AbstractUser):
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=8)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=255, default="N/A")
    razao_social = models.CharField(max_length=255, default="N/A")
    is_approved = models.BooleanField(default=False)  # Adicionado campo is_approved
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='lojistas'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='lojistas' 
    )

    #como é representado o objeto como string
    def __str__(self):
        return self.username



    def __str__(self):
        return self.username
