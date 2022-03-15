from tkinter import Widget
from turtle import width
from django.db import models
from django.forms import PasswordInput

# Create your models here.

class RegistrationModel(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=25)
    c_password = models.CharField(max_length=25)