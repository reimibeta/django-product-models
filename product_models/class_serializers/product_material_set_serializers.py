from rest_framework import serializers

from product_models.class_models.product_material import ProductMaterialSet


class ProductMaterialSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductMaterialSet
        fields = ['id', 'url', 'material']
