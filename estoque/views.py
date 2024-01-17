from django.shortcuts import render, redirect, HttpResponse
from .models import Produto

def produto(request):
    dados = {
        'dados': Produto.objects.all()
    }
    return render(request, 'produtos/produtos.html', dados)

def info(request, id_produto):
    dados = {
        'dados' : Produto.objects.get(pk=id_produto)
    }
    return render(request, 'Produtos/info.html', dados)