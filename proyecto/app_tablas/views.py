from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *


# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def about(request):

    return render(request,"about.html")

def contacto(request):
    return render(request, "contacto.html")

def lte(request):
    return render(request, "lte.html")

def registro(request):
    return render(request, "register.html")

def clientes(request):
    cliente = Cliente.objects.all()
    return render(request, "clientes.html", {"cliente":cliente})

def regclientes(request):
   nombre=request.POST['name1']
   direccion=request.POST['dic1']
   email=request.POST['ema1']
   tfno=request.POST['tfno1']
   cliente=Cliente.objects.create(
    nombre=nombre, direccion=direccion, email=email, tfno=tfno
   )

   return redirect(request, "clientes.html")
