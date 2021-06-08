from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_models.class_models.product import Product
from product_models.class_models.product_material import ProductMaterial
from product_models.class_serializers.product_material_set_serializers import ProductMaterialSetSerializer


class ProductMaterialSerializer(FlexFieldsModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(
            is_active=True
        ),
        write_only=True
    )

    class Meta:
        model = ProductMaterial
        fields = ['id', 'url', 'product', 'material']
        # expandable_fields = {'product': ProductSerializer, 'material': ProductMaterialSetSerializer}
        expandable_fields = {'material': ProductMaterialSetSerializer}
