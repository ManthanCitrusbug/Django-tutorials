# from django.core.urlresolvers import reverse_lazy
from operator import mod
from urllib import request
from django import views
from django.views.generic import DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
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
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return render(request,'login.html')
    def get(self,request):
        return render(request,'login.html')


class Profile(View):
    def get(self,request):
        user_name = User.objects.get(pk=request.user.id)
        user_data = AddProduct.objects.filter(user=user_name)
        return render(request,'profile_page.html',{'user_data':user_data})


class LogoutUser(View):
    def get(self,request):
        logout(request)
        return redirect('login')
        

class AddProductView(View):
    def get(self,request):
        user_name = User.objects.get(pk=request.user.id)
        category = Category.objects.filter(user=user_name)
        return render(request,'add_product.html',{'category':category})
    def post(self,request):
        name = request.POST['product_name']
        discription = request.POST['product_discription']
        image = request.POST['product_image']
        price = request.POST['product_price']
        category = request.POST['product_category']
        category_val = Category.objects.get(category_name=category)
        user_name = User.objects.get(pk=request.user.id)
        product_data = AddProduct(product_name=name, product_discription=discription, product_image=image, product_price=price, product_category=category_val,user=user_name)
        # print(user_id)
        product_data.save()
        return redirect('profile')


class AddCategory(View):
    def get(self,request):
        return render(request,'add_category.html')
    def post(self,request):
        name = request.POST['category_name']
        user_name = User.objects.get(pk=request.user.id)
        if Category.objects.filter(category_name__icontains=name).exists():
            category_error = "Category is already exists..."
            return render(request,'add_category.html',{'category':category_error})
        else:
            category_data = Category(category_name=name,user=user_name)
            category_data.save()
        return redirect('profile')

class DeleteProduct(DeleteView):
    model = AddProduct
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

class HomePageView(ListView):
    model = AddProduct
    template_name = 'home_page.html'
    paginate_by = 5

    