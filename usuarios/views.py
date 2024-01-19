from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O ususario {usuario} foi criado com sucesso!')
            return redirect('produto')
    else:
        formulario = UserRegisterForm()
    return render(request, 'usuario/registrar.html', {'formulario': formulario})

#def login(request, id_usuario)
    
