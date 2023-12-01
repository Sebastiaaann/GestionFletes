from django.shortcuts import render,redirect
from .models import Conductores
from .forms import ConductoresForm
from django.contrib import messages

def registrarConductores(request):
    conductores = Conductores.objects.all()
    if request.method == 'POST':
        form = ConductoresForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor Registrado Correctamente!')
            return redirect('registrarConductores')
        else:
            messages.error(request, 'Error al registrar el conductor. Por favor, verificar los datos.')
            return render(request,'gestionConductores.html', {"form":form, "conductores":conductores})
    else:
        form = ConductoresForm()
        return render(request,'gestionConductores.html', {"form":form, "conductores":conductores})

def editarConductores(request, conductorID):
    conductor = Conductores.objects.get(conductorID=conductorID)
    if request.method == 'POST':
        form = ConductoresForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor Editado Correctamente!')
            return redirect('registrarConductores')
        else:
            messages.error(request, 'Error al editar el conductor. Por favor, verifica los datos.')
            return render(request, 'edicionConductores.html', {'form':form,"conductorID":conductorID})
    else:
        form = ConductoresForm(instance=conductor)
        return render(request, 'edicionConductores.html', {'form':form,"conductorID":conductorID})

def eliminarConductores(request,conductorID):
    conductores = Conductores.objects.get(conductorID=conductorID)
    conductores.delete()
    messages.success(request, 'Conductor Eliminado Correctamente!')
    return redirect('registrarConductores')


