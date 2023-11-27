from django.urls import path
from . import views

urlpatterns = [
    path('homeMantenciones/', views.homeMantenciones, name="homeMantencion"),
    path('registrarMantencion/', views.registrarMantencion, name="registrarMantencion"),
    path('eliminarMantencion/<codigo>', views.eliminarMantencion, name="eliminarMantencion"),
    path('edicionMantencion/<codigo>', views.edicionMantencion, name="edicionMantencion"),
    path('editarMantencion/"', views.editarMantencion, name="editarMantencion"),
]