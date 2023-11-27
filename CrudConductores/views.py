from django.shortcuts import render,redirect
from .models import Conductores
from django.contrib import messages
# Create your views here.

def homeConductores(request):
    conductoresListados = Conductores.objects.all()
    
    return render(request, 'gestionConductores.html', {'conductores':conductoresListados,})


def registrarConductor(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtAppellido']
    fechaNacimiento=request.POST['txtDateNacimiento']
    direccion=request.POST['txtDireccion']
    numeroLicencia=request.POST['txtNlicencia']
    otrosDetalles=request.POST['txtOtrosDetalles']

    conductores = Conductores.objects.create(rut=rut, nombre=nombre, apellido=apellido, fechaNacimiento=fechaNacimiento, 
                                             direccion=direccion, numeroLicencia=numeroLicencia, otrosDetalles=otrosDetalles)
    messages.success(request, 'Conductor Registrado Correctamente!')
    return redirect('HomeConductores')


def eliminacionConductor(request,rut):
    conductores = Conductores.objects.get(rut=rut)
    conductores.delete()

    messages.success(request, 'Conductor Eliminado Correctamente!')

    return redirect('HomeConductores')

def edicionConductor(request,rut):
    conductores = Conductores.objects.get(rut=rut)
    return render(request, 'edicionConductor.html', {'conductores':conductores,})

def editarConductor(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtAppellido']
    fechaNacimiento=request.POST['txtDateNacimiento']
    direccion=request.POST['txtDireccion']
    numeroLicencia=request.POST['txtNlicencia']
    otrosDetalles=request.POST['txtOtrosDetalles']

    conductores = Conductores.objects.get(rut=rut)

    conductores.rut=rut
    conductores.nombre=nombre
    conductores.apellido=apellido
    conductores.fechaNacimiento=fechaNacimiento
    conductores.direccion=direccion
    conductores.numeroLicencia=numeroLicencia
    conductores.otrosDetalles=otrosDetalles
    conductores.save()

    messages.success(request, 'Conductor Editado Correctamente!')

    return redirect('HomeConductores')




