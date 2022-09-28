from main_site import models
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # specifyed our model to work with
        model = models.ProductModel
        # we want all the fields to share so we have used '__all__' eather we can use fields
        fields = '__all__'
        