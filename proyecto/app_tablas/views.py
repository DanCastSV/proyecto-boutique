from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def index(request):
    
    return render(request, 'index.html')


def about(request):

    return render(request,"about.html")

def contacto(request):
    return render(request, "contacto.html")

def inicio(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
         login(request, user)
        return redirect('principal/')
    return render(request, "lte.html")

def logot(request):
    logout(request)
    return redirect("/")


class Registro(UserCreationForm):
    class Meta:
        model = User 
        fields=['username','password1','password2','email','first_name','last_name']

    
def registro(request):
    form=Registro()
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
           form.save()
          
    return render(request, "register.html", {"form":form})

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

def aggpedido(request):
    numero=request.POST['num']
    fecha=request.POST['date']
    pedido= Pedido.objects.create(
     numero=numero, fecha=fecha)

    

    return redirect('/pedidos')


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

def playerasfut(request):

    return render (request, "playerasfut.html")

def pedido(request):
    pedido = Pedido.objects.all()

    return render (request, 'pedidos.html', {"pedido":pedido})

def registrarped (request):

    return HttpResponse 