from rest_framework import serializers

from product_models.products.class_models.product_size import ProductSizeFormatSet


class ProductSizeFormatSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductSizeFormatSet
        fields = '__all__'
