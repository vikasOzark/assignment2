from rest_framework import viewsets  
from main_site import models
from . import serializers

# Classe based viewset 
class ProductViewsetView(viewsets.ModelViewSet):
    # Overring the loonkup field to perform lookup with slug field
    lookup_field = 'slug'

    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    