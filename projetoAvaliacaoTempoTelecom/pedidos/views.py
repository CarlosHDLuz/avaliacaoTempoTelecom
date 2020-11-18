from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import Http404, HttpResponseRedirect

from .models import Cliente, Produto

import datetime


def index(request):
    Cliente.objects.get_or_create(
        nome='Carlos Henrique Duarte Luz',
        telefone=5562991837421,
        data_nascimento=datetime.date(1993, 4, 19)
    )
    Produto.objects.get_or_create(
        nome='Batata',
        valor='2.00'
    )
    return render(request, 'pedidos/index.html')


def clientes(request):
    latest_clientes_list = Cliente.objects.order_by('-created_at')
    context = {
        'latest_clientes_list': latest_clientes_list,
    }
    return render(request, 'pedidos/clientes.html', context)


def cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise Http404("Cliente não existe!")
    return render(request, 'pedidos/cliente.html', {'cliente': cliente})


def produtos(request):
    latest_produtos_list = Produto.objects.order_by('-created_at')
    return render(request, 'pedidos/produtos.html', {'latest_produtos_list': latest_produtos_list})
