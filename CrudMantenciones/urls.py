from django.urls import path
from . import views

urlpatterns = [
    path('registrarMantenciones/', views.registrarMantenciones, name="registrarMantenciones"),
    path('editarMantenciones/<mantencionID>', views.editarMantenciones, name="editarMantenciones"),
    path('eliminarMantenciones/<mantencionID>', views.eliminarMantenciones, name="eliminarMantenciones"),
]