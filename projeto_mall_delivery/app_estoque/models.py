from django.db import models
from app_cadastro.models import Lojista

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    lojista = models.ForeignKey(Lojista, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self) -> str:
        return self.nome
    
    