from django.db import models

# Create your models here.
class Conductores(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaNacimiento = models.DateTimeField()
    direccion = models.CharField(max_length=100)
    numeroLicencia = models.CharField(max_length=10)
    otrosDetalles = models.CharField(max_length=100)

    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5} {6}"
        return texto.format(self.rut, self.nombre, self.apellido, self.fechaNacimiento, self.direccion, self.numeroLicencia, self.otrosDetalles)
