from urllib import request
from django.shortcuts import render

# Create your views here.
def registration_form(request):
    return render(request,'reg_page/registration_form.html')

def login(request):
    return render(request,'reg_page/try.html')