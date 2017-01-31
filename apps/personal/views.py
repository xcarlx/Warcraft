# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, PersonaForm
from .models import Persona
import json
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def Perfil(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
		persona = Persona.objects.get(usuario = request.user)
		return render(request, 'perfil.html', {'persona':persona})

def EditarPerfil(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			formuser = UserForm(request.POST, instance=request.user)
			persona = Persona.objects.get(usuario = request.user)
			# formpersona = PersonaForm(request.POST, request.FILES)
			formpersona = PersonaForm(request.POST, request.FILES, instance = persona)
			# password = str(request.POST['password'] if request.POST['password'] else "")
			# form = PasswordChangeForm(user=request.user, data=request.POST)
			if formuser.is_valid():
				if formpersona.is_valid():
					# if form.is_valid():
					# 	form.save()
					# 	update_session_auth_hash(request, form.user)
					formuser.save()
					formpersona.save()
					
					data = {"ok":True}
					return HttpResponse(json.dumps(data), content_type='application/json')
					
				else:
					return render(request, 'formulario.html',
					{'form':formuser,'form1':formpersona,})
					
			else:
				return render(request, 'formulario.html',
					{'form':formuser,'form1':formpersona,})
			
		else:
			edit_form = UserForm(instance=request.user)
			persona = Persona.objects.get(usuario = request.user)
			persona_form = PersonaForm(instance = persona)
			return render(request, 'formulario.html',
				{
					'form':edit_form,'form1':persona_form,
				})