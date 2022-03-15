from urllib import request
from django.shortcuts import render
from django.views import View
from .models import RegistrationModel
from .forms import Registration
# Create your views here.
class Registration(View):
    def get(self,request):
        reg = Registration(request.POST)
        return render(request,'register.html',{'registration':reg})
    def post(self):
        reg = Registration()]
        if reg.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            c_password = request.POST['c_password']
            regi_model = RegistrationModel(name=name,email=email,password=password,c_password=c_password)
            regi_model.save()
        return render(request,'register.html',{'registeration':reg})
