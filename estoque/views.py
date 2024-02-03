from django.shortcuts import render, redirect, HttpResponse
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

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


@login_required
def criar(request):
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto_form.save()
        return redirect('produto') 
    else:   
        produto_form = ProdutoForm()
        formulario = {
            'formulario': produto_form
        }
        return render(request, 'Produtos/novo_produto.html', context=formulario)


@login_required
def editar(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)   
    if request.method == 'GET':
        formulario = ProdutoForm(instance=produto)
        return render(request, 'Produtos/novo_produto.html', {'formulario': formulario})
    else:
        formulario = ProdutoForm(request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
        return redirect('produto')


@login_required
def excluir(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    if request.method == 'GET':
        return render(request, 'Produtos/confirmar_exclusao.html', {'item': produto})
    else:
        produto.delete()
        return redirect('produto')
    
