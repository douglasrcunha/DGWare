from django.shortcuts import render, redirect, HttpResponse

def produto(request):
    return render(request, 'produtos/produtos.html')