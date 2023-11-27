from django.db import models


# Create your models here.
class Vehiculos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    patente= models.CharField(max_length=7)
    fechaAdquisicion = models.DateTimeField()
    fechaUltimoMant = models.DateTimeField()
    otrosDetalles = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)

    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5} {6} {7}"
        return texto.format(self.codigo, self.nombre, self.modelo, self.patente, self.fechaAdquisicion, self.fechaUltimoMant, self.otrosDetalles, self.estado)