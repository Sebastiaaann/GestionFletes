from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recorridos
from .forms import RecorridosForm

def registrarRecorridos(request):
    recorridos = Recorridos.objects.all()
    if request.method == 'POST':
        form = RecorridosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recorrido Registrado Correctamente!')
            return redirect('registrarRecorridos')
        else:
            messages.error(request, 'Error al registrar el recorrido. Por favor, verificar los datos.')
            return render(request,'gestionRecorrido.html', {"form":form, "recorridos":recorridos})
    else:
        form = RecorridosForm()
        return render(request,'gestionRecorrido.html', {"form":form, "recorridos":recorridos})

def editarRecorridos(request, recorridoID):
    recorrido = Recorridos.objects.get(recorridoID=recorridoID)
    if request.method == 'POST':
        form = RecorridosForm(request.POST, instance=recorrido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recorrido Editada Correctamente!')
            return redirect('registrarRecorridos')
        else:
            messages.error(request, 'Error al editar el recorrido. Por favor, verifica los datos.')
            return render(request, 'editarRecorrido.html', {'form':form,"recorridosID":recorridosID})
    else:
        form = RecorridosForm(instance=recorrido)
        return render(request, 'editarRecorrido.html', {'form':form,"recorridosID":recorridosID})


def eliminarRecorridos(request, recorridoID):
    recorrido = Recorridos.objects.get(recorridoID=recorridoID)
    recorrido.delete()
    messages.success(request, 'Recorrido eliminado exitosamente!')
    return redirect('registrarRecorridos')
  
