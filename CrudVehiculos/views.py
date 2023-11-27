from django.shortcuts import render, redirect
from .models import Vehiculos
from django.contrib import messages

# Create your views here.
def home(request):
    vehiculosListados = Vehiculos.objects.all()
    
    return render(request,"GestionFletes.html", { "vehiculos": vehiculosListados})


def registarVehiculo(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    modelo=request.POST['txtModelo']
    patente=request.POST['numPatente']
    fechaAdquisicion=request.POST['txtfechaAdquisicion']
    fechaUltimoMant=request.POST['txtFechaUltimoMant']
    otrosDetalles=request.POST['txtOtrosDetalles']
    estado=request.POST['txtEstado']

    vehiculo=Vehiculos.objects.create(codigo=codigo, nombre=nombre, modelo=modelo, patente=patente, fechaAdquisicion=fechaAdquisicion, 
                                      fechaUltimoMant=fechaUltimoMant, otrosDetalles=otrosDetalles, estado=estado)
    messages.success(request, 'Vehiculo registrado correctamente')
    return redirect('/')

def edicionVehiculo(request, codigo):
    vehiculo = Vehiculos.objects.get(codigo=codigo)
    return render(request, "edicionVehiculo.html", {"vehiculo": vehiculo})

def editarVehiculo(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    modelo=request.POST['txtModelo']
    patente=request.POST['numPatente']
    fechaAdquisicion=request.POST['txtfechaAdquisicion']
    fechaUltimoMant=request.POST['txtFechaUltimoMant']
    otrosDetalles=request.POST['txtOtrosDetalles']
    estado=request.POST['txtEstado']

    vehiculo = Vehiculos.objects.get(codigo=codigo)
    vehiculo.nombre=nombre
    vehiculo.modelo=modelo
    vehiculo.patente=patente
    vehiculo.fechaAdquisicion=fechaAdquisicion
    vehiculo.fechaUltimoMant=fechaUltimoMant
    vehiculo.otrosDetalles=otrosDetalles
    vehiculo.estado=estado
    vehiculo.save()
    
    messages.success(request, 'Vehiculo editado correctamente!')

    return redirect('/')


def delVehiculo(request, codigo):
    vehiculo = Vehiculos.objects.get(codigo=codigo)
    vehiculo.delete()
    
    messages.success(request, 'Vehiculo eliminado correctamente!')
    return redirect('/')