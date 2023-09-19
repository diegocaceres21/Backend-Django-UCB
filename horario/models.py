from django.db import models

# Create your models here.
class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=20, blank=False)
    asignatura = models.TextField(blank=False)
    paralelo = models.PositiveSmallIntegerField(blank=False)
    horario = models.TextField()

    def __str__(self):
        return self.asignatura   

class Opcion(models.Model):
    id = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=200,blank=False)
    opcion = models.PositiveSmallIntegerField(blank=False)
    horario = models.ManyToManyField(Horario)

    def __str__(self):
        return self.carrera + " Opcion: " + str(self.opcion)
##Falta colocar carrera y numero de opcion