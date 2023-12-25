from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from CrudVehiculos.models import Vehiculos
from django.db.models import Sum
from IngresosEgresos.models import Ingresos, Egresos

@login_required
def balance(request):
    vehiculos_inactivos = Vehiculos.objects.filter(estado='inactivo').count()
    vehiculos_activos = Vehiculos.objects.filter(estado='activo').count()

    ingresos = Ingresos.objects.all()
    egresos = Egresos.objects.all()

    total_ingresos = ingresos.aggregate(total=Sum('valor'))['total']
    total_egresos = egresos.aggregate(total=Sum('valor'))['total']

    total_ingresos = total_ingresos if total_ingresos is not None else 0
    total_egresos = total_egresos if total_egresos is not None else 0

    saldo_total = total_ingresos - total_egresos

    context = {
        'total_ingresos': total_ingresos,
        'total_egresos': total_egresos,
        'saldo_total': saldo_total,
        'vehiculos_inactivos': vehiculos_inactivos,
        'vehiculos_activos': vehiculos_activos,
        }
    return render(request, 'Balance.html', context)
