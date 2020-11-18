from django.forms import ModelForm

from .models import Cliente, Produto, Pedido


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'data_nascimento']


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'valor']


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'produto', 'valor_total']
