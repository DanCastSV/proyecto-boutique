from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contacto/', contacto),
    path('lte/', lte),
    path('registro/', registro)

]
