from django.urls import path
from . import views

app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),

    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:cliente_id>/', views.cliente, name='cliente'),
]

