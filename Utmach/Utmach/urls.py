from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from apps.notas.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Utmach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$',TemplateView.as_view(template_name='inde.html'),name='sistema'),
   # url(r'^$',TemplateView.as_view(template_name='login.html'),name='sistema'),
    url(r'^$', login.as_view(),name='login'),
    url(r'^notas/',include('apps.notas.urls')),


)


