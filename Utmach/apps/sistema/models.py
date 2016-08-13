# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User




class TipoPersona(models.Model):
    descipcion=models.CharField(max_length=20,verbose_name=u"Descripcion:")
    def __unicode__(self):
        return self.descipcion 

class EstadoPersona(models.Model):
    estado=models.CharField(max_length=8,verbose_name=u"Estado:")
    def __unicode__(self):
        return self.estado

class Persona(models.Model):
    cedula = models.CharField(max_length=10,verbose_name=u"Cedula:")
    nombre = models.CharField(max_length=50,verbose_name=u"Nombre:")
    apellido = models.CharField(max_length=80,verbose_name=u"Apellido:")
    telefono = models.CharField(max_length=10, blank=True,verbose_name=u"Telefono:")
    celular = models.CharField(max_length=10, blank=True,verbose_name=u"Celular:")
    direccion = models.CharField(max_length=200,verbose_name=u"Direccion:")
    email = models.EmailField(verbose_name=u"Email:")
    tipo = models.ForeignKey(TipoPersona, blank=True, null=True,verbose_name=u"Tipo:")
    estado = models.ForeignKey(EstadoPersona, blank=True, null=True,verbose_name=u"Estado:")

    def __unicode__(self):
        return self.nombre +" "+ self.apellido






class Estudiante(models.Model):
    contrasena = models.CharField(max_length=50,verbose_name=u"Contrasena:")
    persona = models.ForeignKey(Persona, blank=True, null=True,verbose_name=u"Persona:")

    def __unicode__(self):
        return self.persona.nombre +" "+ self.persona.apellido


class Docente(models.Model):
    contrasena = models.CharField(max_length=50,verbose_name=u"Contrasena:")
    persona = models.ForeignKey(Persona, blank=True, null=True,verbose_name=u"Persona:")

    def __unicode__(self):
        return self.persona.nombre +" "+ self.persona.apellido



class Materia(models.Model):
    nombre = models.CharField(max_length=80,verbose_name=u"Nombre:")
    profesor = models.ForeignKey(Docente, blank=True, null=True,verbose_name=u"Docente:")

    def __unicode__(self):
        return self.nombre

class Paralelo(models.Model):
    descipcion = models.CharField(max_length=40,verbose_name=u"Paralelo:")
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.descipcion


class EstadoMatricula(models.Model):
    estado=models.CharField(max_length=10,verbose_name=u"Estado:")
    
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.estado

class Nivel(models.Model):
    descipcion = models.CharField(max_length=40,verbose_name=u"Nivel:")
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.descipcion

class Periodo(models.Model):
    periodo=models.CharField(max_length=10,verbose_name=u"Periodo:")
    
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return self.periodo

class Hora(models.Model):
    inicio=models.TimeField(verbose_name=u"Hora Inicio:")
    fin=models.TimeField(verbose_name=u"Hora Fin:")
    
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return str(self.inicio)+" - "+str(self.fin)

class Matricula(models.Model):
    nivel = models.ForeignKey(Nivel, blank=True, null=True,verbose_name=u"Nivel:")
    ano = models.DateField(verbose_name=u"Año:")
    periodo = models.ForeignKey(Periodo, blank=True, null=True,verbose_name=u"Periodo:")
    horario=models.ForeignKey(Hora, blank=True, null=True,verbose_name=u"Horario:")
    estado = models.ForeignKey(EstadoMatricula, blank=True, null=True,verbose_name=u"Estado:")
    estudiante=  models.ForeignKey(Estudiante, blank=True, null=True,verbose_name=u"Estudiante:")
    paralelo = models.ForeignKey(Paralelo, blank=True, null=True,verbose_name=u"Paralelo:")
    materia = models.ForeignKey(Materia, blank=True, null=True,verbose_name=u"Materia:")
    
    class Meta:
        ordering = ["id"]
    def __unicode__(self):
        return "N° "+ str(self.id)

class Nota(models.Model):
    deberes = models.FloatField(verbose_name=u"Deberes:")
    participacionClases = models.FloatField(verbose_name=u"Participacion:")
    oral = models.FloatField(verbose_name=u"Leccion oral:")
    escrita = models.FloatField(verbose_name=u"Leccion Escrita:")
    examen = models.FloatField(verbose_name=u"Examen:")
    total = models.FloatField(verbose_name=u"Total:")
    matricula = models.ForeignKey(Matricula, blank=True, null=True,verbose_name=u"Matricuala:")

    def __unicode__(self):
        return "Nota: "+str(self.matricula.estudiante)


class Sesion(models.Model):
    usuario = models.ForeignKey(Persona, blank=True, null=True,verbose_name=u"Persona:")

    def __unicode__(self):
        return "Bienvenido "+str(self.usuario.nombre)+" "+str(self.usuario.apellido)


