from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.views import View
from .models import Register
from .forms import RegiForm

# Create your views here.

# def regi(request):
#     if request.method == 'POST':
#         reg = RegiForm(request.POST)
#         if reg.is_valid():
#             name = reg.cleaned_data['name']
#             age = reg.cleaned_data['age']
#             phone = reg.cleaned_data['phone']
#             email = reg.cleaned_data['email']
#             password = reg.cleaned_data['password']
#             c_password = reg.cleaned_data['c_password']
#             regi_m = Register(name=name,age=age,phone=phone,email=email,password=password,c_password=c_password)
#             regi_m.save()
#             reg = RegiForm()
#     else:
#         reg = RegiForm()
#     return render(request,'index.html',{'regi':reg})

def home(request):
    reg = Register.objects.all()
    return render(request,'home.html',{'reg':reg})



class Regi(View):
    def get(self,request):
        reg= RegiForm()
        return render(request,'index.html',{'regi':reg})
    
    def post(self,request):
        reg = RegiForm(request.POST)
        if reg.is_valid():
            name = reg.cleaned_data['name']
            age = reg.cleaned_data['age']
            phone = reg.cleaned_data['phone']
            email = reg.cleaned_data['email']
            password = reg.cleaned_data['password']
            c_password = reg.cleaned_data['c_password']
            regi_m = Register(name=name,age=age,phone=phone,email=email,password=password,c_password=c_password)
            regi_m.save()
            reg = RegiForm()
        return render(request,'index.html',{'regi':reg})