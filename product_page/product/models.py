from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AddProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_disc = models.TextField()
    product_image = models.ImageField(upload_to = 'image')
    product_price = models.FloatField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return self.product_name