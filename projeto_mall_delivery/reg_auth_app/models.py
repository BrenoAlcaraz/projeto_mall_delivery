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
        related_name='consumidor_groups'  # Nome único e válido
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='consumidor_permissions'  # Nome único e válid
    )

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
        related_name='lojista_groups'  # Nome único e válido
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='lojista_permissions'  # Nome único e válido
    )
