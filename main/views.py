# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from main.forms import UserForm
from django.contrib.auth.models import User

def home(request):
	contexto = ''
	if not request.user.is_anonymous():
		usuario = request.user
		contexto = {'usuario':usuario}
	return render(request,'home.html',contexto)
#Registro temporal
def nuevo_usuario(request):
	if request.user.is_anonymous():
		if request.method == 'POST':
			formulario = UserCreationForm(request.POST)
			if formulario.is_valid:
				formulario.save()
				return HttpResponse('/')
		else: 
			formulario = UserCreationForm()
		return render(request, 'registration/registro.html', {'form':formulario})
	else:
		return HttpResponseRedirect('/')
""" (Esto hace juego con main.forms.py)
def nuevo_usuario(request):
	if request.method == 'POST':
		formulario = UserForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserForm()
	return render(request, 'registration/registro.html',{'form':formulario})
"""