from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User ,AbstractUser
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class AddProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_discription = models.TextField()
    product_image = models.ImageField(upload_to = 'image')
    product_price = models.PositiveIntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.product_name


# class User(AbstractUser):
#     products = models.ForeignKey(AddProduct, on_delete=models.CASCADE, default="")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

#     def __str__(self):
#         return self.username