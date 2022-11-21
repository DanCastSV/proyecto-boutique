from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contacto/', contacto),
    path('lte/', lte),
    path('registro/', registro),
    path('clientes/', clientes),
    path('regclientes/', regclientes),
    path('elimclientes/<id>', elimclientes),
    path('editclientes/<id>', editclientes),
    path('guarclientes/<id>', guarclientes)
    

]
