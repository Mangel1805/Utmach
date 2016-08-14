from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
  
    #url(r'^registrar/$', crearDispositivo.as_view(),name='crear_Dispositivo'),
    #url(r'^editar/(?P<pk>[\d]+)$', editarDispositivo.as_view(),name='editar_Dispositivo'),
    #url(r'^eliminar/(?P<pk>[\d]+)$', eliminarDispositivo.as_view(),name='eliminar_Dispositivo'),
    url(r'^listar/$', listarNota.as_view(),name='listar_Notas'),
    url(r'^validar/$', validarLogin,name='validar'),
    url(r'^salir/$', 'apps.notas.views.salir', name='salir'),
    url(r'^solicitud/$', solicitud.as_view(),name='solicitud'),
    url(r'^imprimir/$', imprimir.as_view(),name='imprimir'),
    ) 