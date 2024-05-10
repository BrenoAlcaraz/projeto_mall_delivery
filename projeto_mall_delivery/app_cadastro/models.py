from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class Consumidor(AbstractUser):
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='consumidor_groups'  # Adicione um related_name único
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='consumidor_permissions'  # Adicione um related_name único
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
        related_name='lojista_groups'  # Adicione um related_name único
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='lojista_permissions'  # Adicione um related_name único
    )

class Admin(AbstractUser):
    pass
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='admin_groups'  # Adicione um related_name único
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='admin_permissions'  # Adicione um related_name único
    )