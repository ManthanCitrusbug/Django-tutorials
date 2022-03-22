from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.


class Index(View):
    def get(self,request):
        return render(request,'index.html')


class Register(View):
    def get(self,request):
        return render(request,'registration.html')
    def post(self,request):
        # form = User.objects.all()
        uname = request.POST['username']
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['password']
        # confirm_password = request.POST['c_password']
        user = User(username=uname,first_name=fname,last_name=lname,email=email)
        user.save()
        user.set_password(password)
        user.save()
        return redirect('login')


class LoginUser(View):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print('login')
            return redirect('profile')
        else:
            print('error')
            return render(request,'login.html')
    def get(self,request):
        return render(request,'login.html')


class Profile(View):
    def get(self,request):
        return render(request,'profile_page.html')


class LogoutUser(View):
    def get(self,request):
        logout(request)
        return redirect('login')
        

class AddProduct(View):
    def get(self,request):
        form = ProductForm()
        return render(request,'add_product.html',{'form':form})
    def post(self,request):
        name = request.POST['product_name']
        discription = request.POST['product_discription']
        image = request.POST['product_image']
        price = request.POST['product_price']
        category = request.POST['product_category']
        product_data = AddProduct(product_name=name, product_discription=discription, product_image=image, product_price=price, product_category=category)
        print(product_data)
        # product_data.save()
        return redirect('profile')


class AddCategory(View):
    def get(self,request):
        form = CategoryForm()
        return render(request,'add_category.html',{'form':form})
    def post(self,request):
        name = request.POST['category_name']
        category_data = Category(category_name=name)
        category_data.save()
        return redirect('profile')