from unittest import TextTestRunner
from django.db import models

# Create your models here.
class ProductModel(models.Model):
    slug = models.SlugField(unique=True) # slug field optimaize our serches 
    product_name = models.CharField(max_length=50)
    discription = models.CharField(max_length=200)
    price = models.FloatField()
    product_img = models.ImageField()