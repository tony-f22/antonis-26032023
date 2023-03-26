from rest_framework import serializers
from .models import Product, Image


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ('url', 'path', 's3_url', 's3_url_resized')


#
#
# class ProductSerializer(serializers.ModelSerializer):
#     images = ImageSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Product
#         fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('_id', 'gender', 'product_id', 'product_title', 'images')

# from rest_framework_mongoengine import serializers
#
# from products.models import Product
#
#
# class ProductSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Product
#         fields = ('product_id', )
#         # fields = '__all__'
