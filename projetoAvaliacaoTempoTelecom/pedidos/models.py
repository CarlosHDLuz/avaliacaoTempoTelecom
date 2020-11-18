from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, help_text="Formato: 1234567.89")
    # Valor máximo 9 999 999 999,99 -> 12 dígitos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    # Exemplo de telefone: 55 62 99183 7421 -> 13 dígitos
    telefone = models.DecimalField(max_digits=13, decimal_places=0, null=False, help_text="Formato: 5562912345678")
    data_nascimento = models.DateField(null=False, help_text="Formato: dd/mm/aaaa")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    # numero do pedido -> id, auto incrementado e único para cada objeto/tupla do banco
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
