# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout	

def home(request):
	return render(request,'home.html')