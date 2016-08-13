from django.shortcuts import render,render_to_response,get_object_or_404
from apps.sistema.models import *
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, RequestContext, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers
from django.db import transaction
from django.contrib import messages

from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect

def salir(request):
	prueba = Sesion.objects.all()
	prueba.delete()
	return HttpResponseRedirect("http://localhost:8000/")

class listarNota(ListView):
	template_name='notas/listarNota.html'
	context_object_name='nota'
	model=Nota
	def get_context_data(self,**kwargs):
		ctx = super(listarNota, self).get_context_data(**kwargs)
		ctx['persona'] = Persona.objects.all()
		ctx['sesion'] = Sesion.objects.all()
		ctx['matricula']=Matricula.objects.all()
		return ctx

class login(ListView):
	template_name='login.html'
	context_object_name='personas'
	model=Persona
	def get_context_data(self,**kwargs):
		ctx = super(login, self).get_context_data(**kwargs)
		ctx['estudiantes'] = Estudiante.objects.all()
		ctx['docente'] = Docente.objects.all()
		return ctx



def validarLogin(request):
	print "ENTROOOOO :V :v "
	cedula=request.GET['cedula']
	contra=request.GET['contra']
	persona=Persona.objects.get(cedula=cedula)
	print cedula
	print persona

	s=Sesion(usuario=persona)
	s.save()
	print "se guardo"
	template_name='notas/listar.html'
	
	
