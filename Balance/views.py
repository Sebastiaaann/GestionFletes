from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from CrudVehiculos.models import Vehiculos
from django.db.models import Sum
from IngresosEgresos.models import Ingresos, Egresos
from CrudRecorridos.models import Recorridos
from CrudConductores.models import Conductores

@login_required
def balance(request):
    # Vehicles
    vehiculos_inactivos = Vehiculos.objects.filter(estado='inactivo').count()
    vehiculos_activos = Vehiculos.objects.filter(estado='activo').count()
    total_vehiculos = Vehiculos.objects.count()

    # Conductores
    total_conductores = Conductores.objects.count()

    # Recorridos
    total_recorridos = Recorridos.objects.count()
    recientes = Recorridos.objects.order_by('-fecha')[:5]

    # Finanzas
    ingresos = Ingresos.objects.all()
    egresos = Egresos.objects.all()

    total_ingresos = ingresos.aggregate(total=Sum('valor'))['total'] or 0
    total_egresos = egresos.aggregate(total=Sum('valor'))['total'] or 0
    saldo_total = total_ingresos - total_egresos

    # Utilización simple: porcentaje vehículos activos
    utilizacion = 0
    if total_vehiculos > 0:
        utilizacion = round((vehiculos_activos / total_vehiculos) * 100)

    context = {
        'total_ingresos': total_ingresos,
        'total_egresos': total_egresos,
        'saldo_total': saldo_total,
        'vehiculos_inactivos': vehiculos_inactivos,
        'vehiculos_activos': vehiculos_activos,
        'total_vehiculos': total_vehiculos,
        'total_conductores': total_conductores,
        'total_recorridos': total_recorridos,
        'recientes': recientes,
        'utilizacion': utilizacion,
    }
    return render(request, 'Dashboard.html', context)
