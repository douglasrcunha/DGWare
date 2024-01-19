"""
URL configuration for DGWare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from estoque import views
from usuarios import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    #path('login/', usuario_views.login, name='login'),
    path('', views.produto, name='produto'),
    path('novo_produto', views.criar, name='novo_produto'),
    path('novo_produto/<int:id_produto>', views.editar, name='editar'),
    path('excluir_produto/<int:id_produto>', views.excluir, name='excluir'),
    path('<int:id_produto>', views.info, name='info'),
]
