from django.shortcuts import render
from apps.sistema.models import *
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers
from django.db import transaction
from django.contrib import messages
