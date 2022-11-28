from django.test import TestCase
from app_tablas.models import *

class TestModels(TestCase):
    def test_create(self):
     self.clienteprueba = Cliente.object.create(
         nombre = "Daniel",
         direccion = "col. ciudad pacifica",
         email = "ec1335854@gmail.com",
         tfno = "78562548"
         )