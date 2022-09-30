from contextlib import nullcontext
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=50)
    # slug = AutoSlugField(populate_from=['product_name'])  # slug field optimaize our serches 
    slug = models.SlugField(blank=True, editable=False)
    discription = models.CharField(max_length=200)
    price = models.FloatField()
    product_img = models.ImageField()
    

    def __str__(self):
        return f'{self.product_name} -> {self.price}'

    def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug name
        self.slug = slugify(self.product_name)
        #this line below save every fields of the model instance
        super(ProductModel, self).save(*args, **kwargs) 