# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from ..personal.models import Persona
import json
# Create your views here.

def Inicio(request):
	if(request.session.get("idusuario", False)):
		template = loader.get_template('inicio.html')
		persona = Persona.objects.get(usuario = request.user)
		return HttpResponse(template.render({'persona':persona}, request))
		# pass
	else:
		return render(request, 'inicio.html')



def Login(request):
	if(request.session.get("idusuario", False)):
		# template = loader.get_template('inicio.html')
		# return HttpResponse(template.render({}, request))
		return HttpResponseRedirect('/')
	else:
		p = request.POST
		response_data = {}
		if request.method == 'POST':
			user = authenticate(username= p['txtusuario'], password= str(p['txtpassword']))
			if user is not None:
				login(request, user)
				request.session['idusuario'] = user.id
				try:
					request.session['persona'] = user.first_name+" "+user.last_name
					request.session['estado'] = True
					request.session['email'] = user.email
					
					# menu = Menu.objects.all().order_by('menupadre', 'orden')
					# menus = []
					# for menu in menu:
					# 	menus.append({"nombre":menu.nombre, "ruta":menu.ruta, "menupadre":menu.menupadre.nombre if menu.menupadre else None })
					# request.session['menu'] = menus

				except ObjectDoesNotExist :
					request.session['persona'] = "Anonimo"
				response_data['result'] = True
				response_data['message'] = 'Bienvenido'
				return HttpResponse(json.dumps(response_data), content_type="application/json")
				# return HttpResponseRedirect('/')
			else:
				response_data['result'] = False
				response_data['message'] = 'Usuario o contraseña son incorrectos'
				return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			return render(request, 'login.html')

def Logout(request):
	logout(request)
	return HttpResponseRedirect('/')
