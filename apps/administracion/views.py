# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import hashlib
from django.contrib.auth import hashers
# from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Create your views here.

def Inicio(request):
	if(request.session.get("idusuario", False)):
		#return render(request, 'inicio.html')
		pass
	else:
		return render(request, 'inicio.html')



def Login(request):
	if(request.session.get("idusuario", False)):
		#return render(request, 'inicio.html')
		pass
	else:
		p = request.POST
		if request.method == 'POST':
			# hasher = PBKDF2PasswordHasher()
			# hasher.encode(password='password',salt='salt',iterations=30000)
			user = authenticate(username= p['txtusuario'], password= hashers.make_password(p['txtpassword'],salt='9mzEh5'))
			print(user)
			if user is not None:
				request.session['idusuario'] = user.id
				try:
					print(user.id)
					# request.session['persona'] = user.firstname+" "+user.lastname
					
					# menu = Menu.objects.all().order_by('menupadre', 'orden')
					# menus = []
					# for menu in menu:
					# 	menus.append({"nombre":menu.nombre, "ruta":menu.ruta, "menupadre":menu.menupadre.nombre if menu.menupadre else None })
					# request.session['menu'] = menus

				except ObjectDoesNotExist :
					request.session['persona'] = "Anonimo"
				return redirect('/')
			else:
				return render( request, 'login.html', {'msj' : "Usuario o contraseña son incorrectas"})
		else:
			return render(request, 'login.html')
