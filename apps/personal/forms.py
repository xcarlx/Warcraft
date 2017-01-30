from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from .models import Persona


class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ( 'first_name', 'last_name', 'email','password')
 		widgets = {
 			'password': forms.PasswordInput(),
 		}
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		# self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})
		# self.fields["password"].widget.attrs['class'] = 'validate'
		self.fields["first_name"].widget.attrs['class'] = 'validate'
		self.fields["last_name"].widget.attrs['class'] = 'validate'
		self.fields["email"].widget.attrs['class'] = 'validate'
	
	# def clean(self):
	# 	cleaned_data = super(UserForm, self).clean()
	# 	password = cleaned_data.get("password")

	# 	if User.check_password(password):
	# 		raise forms.ValidationError(
	# 			"password and confirm_password does not match"
	# 		)

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields = ( 'fnacimiento', 'foto')

	def __init__(self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)
		self.fields["fnacimiento"].widget.attrs['class'] = 'datepicker'
	# 	self.fields["first_name"].widget.attrs['class'] = 'validate'
	# 	self.fields["last_name"].widget.attrs['class'] = 'validate'
	# 	self.fields["email"].widget.attrs['class'] = 'validate'



