from django.contrib import admin

from api.serializers import ProductSerializer
from .models import ProductModel
# Register your models here.
admin.site.register(ProductModel)