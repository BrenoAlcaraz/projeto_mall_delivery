from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _

class Consumidor(AbstractUser):
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='consumidores'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='consumidores' 
    )

    #como é representado o objeto como string
    def __str__(self):
        return self.username

class Lojista(AbstractUser):
    cpf = models.CharField(max_length=14)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=255)

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

    def __str__(self):
        return self.username
