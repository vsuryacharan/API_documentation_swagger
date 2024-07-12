from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='product_images',null=True,blank=True)
    descritiong=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name


