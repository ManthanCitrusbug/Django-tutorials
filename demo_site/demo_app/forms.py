from asyncio.windows_events import NULL
from contextlib import nullcontext
from email.policy import default
from django import forms

class RegiForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    phone = forms.IntegerField()
    # photo = forms.ImageField()
    email = forms.EmailField()
    password = forms.CharField()
    c_password = forms.CharField()