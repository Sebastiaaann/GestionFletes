from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mantenciones
from .forms import MantencionForm

# Create your views here.
def homeMantenciones(request):
    mantenciones = Mantenciones.objects.all()
    form = MantencionForm
    return render(request, 'gestionMantenciones.html', {'mantenciones': mantenciones,'form':form})

def registrarMantencion(request):
    if request == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor Registrado Correctamente!')
            return redirect('homeMantenciones')
    else:
        return redirect('/')


def eliminarMantencion(request,codigo):
    mantencion = Mantenciones.objects.get(codigo=codigo)
    mantencion.delete()

    messages.success(request, 'Mantencion Eliminada Correctamente!')

    return redirect('homeMantenciones')

def edicionMantencion(request,codigo):
    mantencion = Mantenciones.objects.get(codigo=codigo)
    return render(request, 'edicionMantencion.html', {'mantencion':mantencion})

def editarMantencion(request):
    codigo=request.POST['txtCodigo']
    vehiculo=request.POST['txtVehiculo']
    fecha=request.POST['txtFecha']
    valor=request.POST['txtValor']

    mantencion = Mantenciones.objects.get(codigo=codigo)

    mantencion.codigo=codigo
    mantencion.vehiculo=vehiculo
    mantencion.fecha=fecha
    mantencion.valor=valor
    mantencion.save()

    messages.success(request, 'Mantencion Editada Correctamente!')

    return redirect('homeMantenciones')
