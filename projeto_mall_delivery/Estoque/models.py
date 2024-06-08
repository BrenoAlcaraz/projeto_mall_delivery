from django.db import models

# Create your models here.
class Stock(models.Model):
    Categoria = models.CharField(max_length=50,blank=True,null=True)
    nome_item = models.CharField(max_length=50,blank=True,null=True)
    quantidade = models.IntegerField(default=0,null=True,blank=True)
    quantidade_recebida = models.IntegerField(default=0,null=True,blank=True)
    recebida_por= models.CharField(max_length=50,blank=True,null=True)
    quantidade_problema = models.IntegerField(default=0,null=True,blank=True)
    issue_by = models.CharField(max_length=50,blank=True,null=True)
    issue_to = models.CharField(max_length=50,blank=True,null=True)
    numeroTelefone= models.CharField(max_length=50,blank=True,null=True)
    criado_por = models.CharField(max_length=50,blank=True,null=True)
    reorder_level = models.IntegerField(default=0,null=True,blank=True)
    ultima_atualizacao=  models.DateTimeField(auto_now_add=False,auto_now = True)
    exportar_CSV = models.BooleanField(default=False)   

    def __str__(self):
        return self.nome_item + ' [' + str(self.quantidade) + ']'