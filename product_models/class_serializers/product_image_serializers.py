from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_models.class_models.product import Product
from product_models.class_models.product_image import ProductImage
from product_models.class_projects.serializers.product_key_related_field import product_key_related_field


class ProductImageSerializer(FlexFieldsModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(
    #     queryset=Product.objects.filter(
    #         is_active=True
    #     ),
    #     write_only=True
    # )
    product = product_key_related_field.related_field()

    class Meta:
        model = ProductImage
        fields = ['id', 'url', 'product', 'image', 'thumbnail']
