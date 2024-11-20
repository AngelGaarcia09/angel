from django.shortcuts import redirect, render
from .models import Trabajador

# Create your views here.
def inicio_vista(request):
    lostrabajadores=Trabajador.objects.all()
    return render(request,"gestionarTrabajador.html",{"lostrabajadores":lostrabajadores})

def registrarTrabajador(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos" ]

    guardartrabajador=Trabajador.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
        ) #GUARDA EL REGISTRO
    
    return redirect("/")

def seleccionarTrabajador(request,codigo):
        trabajador=Trabajador.objects.get(codigo=codigo)
        return render(request,"editartrabajador.html",{"mistrabajadores": trabajador})

def editartrabajador(request):
        codigo=request.POST["txtcodigo"]
        nombre=request.POST["txtnombre"]
        creditos=request.POST["numcreditos" ]
        trabajador=Trabajador.objects.get(codigo=codigo)
        trabajador.nombre=nombre
        trabajador.creditos=creditos
        trabajador.save() #Guarda registro actualizado
        return redirect("/")

def borrarTrabajador(request,codigo):
    trabajador=Trabajador.objects.get(codigo=codigo)
    trabajador.delete()
    return redirect("/")