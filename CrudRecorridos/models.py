from django.db import models
from CrudConductores.models import Conductores
from CrudVehiculos.models import Vehiculos

class Recorridos(models.Model):
    recorridoID = models.AutoField(primary_key= True)
    conductor = models.ForeignKey(Conductores, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    fecha = models.DateField()
    cargaTransportada = models.CharField(max_length=70)
    rutaRecorrido = models.TextField(max_length=70)
    ganancia = models.PositiveIntegerField()
    gasto = models.PositiveIntegerField()


    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5} {6} {7}"
        return texto.format(self.recorridoID, self.conductor, self.vehiculo, self.fecha, self.rutaRecorrido, self.cargaTransportada, self.ganancia, self.gasto)
    