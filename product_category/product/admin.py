from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_discription','product_price']

admin.site.register(Category)
admin.site.register(AddProduct,ProductAdmin)
