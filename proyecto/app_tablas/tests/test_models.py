from django.test import TestCase
from app_tablas.models import *

class TestModels(TestCase):
    def test_create(self):
     self.clienteprueba = Tallas.object.create(
         talla = "M"
         )