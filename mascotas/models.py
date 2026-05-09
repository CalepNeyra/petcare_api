from django.db import models


class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return self.nombre
