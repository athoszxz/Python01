"""Core views"""
from django.shortcuts import render, redirect
from .models import Pessoa


def home(request):
    """READ: Home page view"""
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})


def salvar(request):
    """CREATE: Salvar pessoa view"""
    vnome = request.POST.get('nome')
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})


def editar(request, id):
    """Ir para página de Editar pessoa view"""
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {'pessoa': pessoa})


def update(request, id):
    """UPDATE: Editar pessoa view"""
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.save()
    return redirect(home)


def deletar(request, id):
    """DELETE: Deletar pessoa view"""
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
