from django.urls import path
from . import views

urlpatterns = [
    path('homeMantenciones/', views.homeMantenciones, name="homeMantenciones"),
    path('registrarMantencion/', views.registrarMantencion, name="registrarMantencion"),
    path('eliminarMantencion/<codigo>', views.eliminarMantencion, name="eliminarMantencion"),
    path('edicionMantencion/<codigo>', views.edicionMantencion, name="edicionMantencion"),
    path('editarMantencion/<codigo>', views.editarMantencion, name="editarMantencion"),
]