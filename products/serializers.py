from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('image_urls', 'product_title', 'product_description', 'price')
