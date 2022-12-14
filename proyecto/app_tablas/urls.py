from django.urls import path
from .views import *

urlpatterns = [
    path('principal/', index),
    path('about/', about),
    path('contacto/', contacto),
    path('', inicio),
    path('cerrarsesion/', logot),
    path('register/', registro),
    path('clientes/', clientes),
    path('regclientes/', regclientes),
    path('elimclientes/<id>', elimclientes),
    path('editclientes/<id>', editclientes),
    path('guarclientes/<id>', guarclientes),
    path('playerasfut/', playerasfut),
    path('pedidos/', pedido),
    path('aggpedido/', aggpedido),
    path('camisash/', camisash),
     path('pantalonesh/', pantalonesh),
     path('shorts/', shorts),
     path('vestidos/', vestidos),
     path('blusas/', blusas)
    

]
