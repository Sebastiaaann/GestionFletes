from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages

# Create your views here.
def regitro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['username']
            messages.success(request, f'Usuario {nombre} creado')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    
    context = {'form': form}

    return render(request, 'registro.html', context)