from django.shortcuts import render, redirect, HttpResponse

def produto(request):
    dados = {
        'nome_produto' : 'sabonete',
        'preco_produto': 3.0,
        'categoria_produto': 'higiene'
    }
    return render(request, 'produtos/produtos.html', dados)