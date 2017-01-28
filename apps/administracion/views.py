# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def Inicio(request):
	if(request.session.get("idusuario", False)):
		template = loader.get_template('inicio.html')
		return HttpResponse(template.render({}, request))
		# pass
	else:
		return render(request, 'inicio.html')



def Login(request):
	if(request.session.get("idusuario", False)):
		template = loader.get_template('inicio.html')
		return HttpResponse(template.render({}, request))
	else:
		p = request.POST
		if request.method == 'POST':
			user = authenticate(username= p['txtusuario'], password= str(p['txtpassword']))
			if user is not None:
				request.session['idusuario'] = user.id
				try:
					# print(user.id)
					request.session['persona'] = user.first_name+" "+user.last_name
					
					# menu = Menu.objects.all().order_by('menupadre', 'orden')
					# menus = []
					# for menu in menu:
					# 	menus.append({"nombre":menu.nombre, "ruta":menu.ruta, "menupadre":menu.menupadre.nombre if menu.menupadre else None })
					# request.session['menu'] = menus

				except ObjectDoesNotExist :
					request.session['persona'] = "Anonimo"
				template = loader.get_template('inicio.html')
				return render( request, 'login.html', {'eval' : True})
			else:
				return render( request, {'msj' : "Usuario o contraseña son incorrectas"})
		else:
			return render(request, 'login.html')
