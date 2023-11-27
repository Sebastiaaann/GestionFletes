from django.db import models
from CrudVehiculos.models import Vehiculos

# Create your models here.
class Mantenciones(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.PositiveIntegerField()

    def __str__(self):
        texto= "{0} {1} {2} {3}"
        return texto.format(self.codigo, self.vehiculo, self.fecha, self.valor)
