import http
from http.client import HTTPResponse
from django.shortcuts import render
from .models import Cliente, Pedido,Articulo
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index():
    return HttpResponse("<h1></h1>")
    