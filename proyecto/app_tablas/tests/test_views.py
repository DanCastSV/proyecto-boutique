from django.test import TestCase, Client
from django.urls import reverse
from app_tablas.models import *

class test_views(TestCase):
    def test_create(self):
     client = Client()

     response = client.get(reverse('principal'))

     self.assertEqual(response.status_code,200)
     self.assertTemplateUsed(response, 'index.html')