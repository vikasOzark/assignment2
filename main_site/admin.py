from django.contrib import admin
from .models import ProductModel

# Register model to perfom CURD task from admin pannel
admin.site.register(ProductModel)