from django.forms import ModelForm

from .models import Cliente, Produto


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'data_nascimento']