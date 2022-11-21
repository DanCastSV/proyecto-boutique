from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm


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
    form=UserCreationForm

    if request.method=="post":
        form=UserCreationForm(request.post)
        if form.is_valid():
            form.save


    context={"form":form}
    return render(request, "register.html", context)

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

   return redirect('/clientes')

def editclientes(request, id):
    cliente=Cliente.objects.get(id=id)
    
    return render(request, 'editcliente.html', {"cliente":cliente})

def guarclientes(request, id):
   nombre=request.POST['name1']
   direccion=request.POST['dic1']
   email=request.POST['ema1']
   tfno=request.POST['tfno1']
   id=Cliente.objects.get(id=id)
   id.nombre=nombre
   id.direccion=direccion
   id.email=email
   id.tfno=tfno
   id.save()

   return redirect('/clientes')

def elimclientes(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/clientes')
