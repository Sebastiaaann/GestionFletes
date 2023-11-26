from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def regitro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['username']
            messages.success(request, f'usuario {nombre} creado')
    else:
        form = UserCreationForm()
    
    context = {'form': form}

    return render(request, 'registro.html', context)