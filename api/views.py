from django.shortcuts import render
from rest_framework import viewsets  
from main_site import models
from . import serializers

# Create your views here.

class ProductViewsetView(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    # lookup_fields = 'slug'

    