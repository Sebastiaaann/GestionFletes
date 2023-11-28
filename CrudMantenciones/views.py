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
    if request.method == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor Registrado Correctamente!')
            return redirect('homeMantenciones')
        else:
            print(form.errors)  # Muestra los errores en la consola para debug
            messages.error(request, 'Error al registrar la mantención. Por favor, verifica los datos.')
    else:
        form = MantencionForm()
    return redirect('/')


def eliminarMantencion(request,codigo):
    mantencion = Mantenciones.objects.get(codigo=codigo)
    mantencion.delete()

    messages.success(request, 'Mantencion Eliminada Correctamente!')

    return redirect('homeMantenciones')

def edicionMantencion(request,codigo):
    mantencion = Mantenciones.objects.get(codigo=codigo)
    form = MantencionForm(request.POST, instance=mantencion)
    return render(request, 'edicionMantenciones.html', {'form':form, 'mantencion': mantencion})

def editarMantencion(request,codigo):
    mantencion = Mantenciones.objects.get(codigo=codigo)
    if request.method == 'POST':
        form = MantencionForm(request.POST, instance=mantencion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantencion Editada Correctamente!')
            return redirect('homeMantenciones')  
    else:
        form = MantencionForm()

    return redirect('/')
