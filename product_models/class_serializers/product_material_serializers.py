from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_models.class_models.product_material import ProductMaterial
from product_models.class_projects.serializers.product_key_related_field import product_key_related_field
from product_models.class_serializers.product_material_set_serializers import ProductMaterialSetSerializer


class ProductMaterialSerializer(FlexFieldsModelSerializer):
    product = product_key_related_field.related_field()

    class Meta:
        model = ProductMaterial
        fields = ['id', 'url', 'product', 'material']
        # expandable_fields = {'product': ProductSerializer, 'material': ProductMaterialSetSerializer}
        expandable_fields = {'material': ProductMaterialSetSerializer}
