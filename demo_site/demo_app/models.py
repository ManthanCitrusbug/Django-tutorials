from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone = models.IntegerField(max_length=10)
    # photo = models.ImageField(upload_to = 'image/',default='')
    email = models.EmailField()
    password = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)