from unittest import TextTestRunner
from django.db import models
from django_extensions.db.models import AutoSlugField

# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=['product_name'])  # slug field optimaize our serches 
    discription = models.CharField(max_length=200)
    price = models.FloatField()
    product_img = models.ImageField()
    

    def __str__(self):
        return f'{self.product_name} -> {self.price}'