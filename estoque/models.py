from django.db import models
from datetime import datetime

class Produto(models.Model):
    nome_produto = models.TextField(max_length=100)
    preco_produto = models.FloatField()
    categoria_produto = models.TextField(max_length=100)
    em_estoque = models.BooleanField(default=False)
    data_in = models.DateField(default=datetime.now)
