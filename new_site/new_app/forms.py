from dataclasses import field
from django import forms
from .models import *
from django.forms import ModelForm

class Registration(ModelForm):
    class Meta():
        model = RegistrationModel
        fields = ['name', 'email', 'phone', 'age', 'password', 'c_password']