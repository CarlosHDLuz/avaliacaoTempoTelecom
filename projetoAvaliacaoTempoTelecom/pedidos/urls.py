from django.urls import path
from . import views

app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),

    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:cliente_id>/', views.cliente, name='cliente'),
    path('novo_usuario/', views.cliente_create, name='cliente_create'),
    path('produtos/', views.produtos, name='produtos'),
    path('novo_produto/', views.produto_create, name='produto_create'),
]

