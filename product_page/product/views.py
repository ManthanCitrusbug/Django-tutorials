from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def add_product(request):
    # category_product = AddProduct.objects.all()
    category_val = Category.objects.all()
    

    if request.method == 'POST':
        name = request.POST['name']
        disc = request.POST['disc']
        image = request.POST['image']
        price = request.POST['price']
        category = request.POST['category']
        add = AddProduct(product_name=name, product_disc=disc, product_image=image, product_price=price, product_category=category)
        add.save()
        # category_prod = AddProduct.objects.all()
        # return HttpResponse(request,'Product Added...')
        return render(request, 'add_product.html',{'category':category_val})
    # else:
        # return render(request,'add_product.html')
    
    return render(request, 'add_product.html',{'category':category_val})