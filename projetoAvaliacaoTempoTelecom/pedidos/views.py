from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import Http404

from .models import Cliente, Produto


def index(request):
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

