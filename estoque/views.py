from django.shortcuts import render, redirect, HttpResponse
from .models import Produto

def produto(request):
    dados = {
        'dados': Produto.objects.all()
    }
    return render(request, 'produtos/produtos.html', dados)