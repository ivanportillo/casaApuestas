from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.core.exceptions import ValidationError

class perfilUsuario(models.Model):
    usuario = models.ForeignKey(User, unique=True)
    dinero = models.FloatField(default=0)
    fechaNacimiento = models.DateField(default=date.today)
    def __str__(self):
        return "%s" % self.usuario.username

    # def clean(self):
    #     fecha_nacimiento_valid = self.fechaNacimiento
    #     fecha_nacimiento_valid=(fecha_nacimiento_valid+timedelta(days=6574))
    #     if fecha_nacimiento_valid >= date.today():
    #         raise ValidationError("El usuario debe ser mayor de edad.")
    #     return super(perfilUsuario,self).clean()

    class Meta:
            verbose_name_plural='Perfiles de usuario'

class Deporte(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return "%s" % self.nombre

class Apuesta(models.Model):
    deporte = models.ForeignKey(Deporte)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    opcion1 = models.CharField(max_length=200)
    cuotaOpcion1 = models.FloatField(default=0)
    opcion2 = models.CharField(max_length=200)
    cuotaOpcion2 = models.FloatField(default=0)
    opcion3 = models.CharField(max_length=200)
    cuotaOpcion3 = models.FloatField(default=0)
    # fechaInicio = models.DateTimeField(auto_now=True, null=True)
    fechaFin = models.DateTimeField(null=True)
    def __str__(self):
        return "%s" % self.titulo

class Participacion(models.Model):
    usuario = models.ForeignKey(perfilUsuario)
    apuesta = models.ForeignKey(Apuesta)
    eleccion = models.PositiveSmallIntegerField()
    cuotaEleccion = models.FloatField(default=0)
    cantidad = models.FloatField()
    class Meta:
        verbose_name_plural='Participaciones'
