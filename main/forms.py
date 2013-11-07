#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']