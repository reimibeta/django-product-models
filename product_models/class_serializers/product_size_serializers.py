from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_models.class_models.product import Product
from product_models.class_models.product_size import ProductSize, ProductSizeFormatSet
from product_models.class_projects.serializers.product_key_related_field import product_key_related_field
from product_models.class_serializers.product_size_format_set_serializers import \
    ProductSizeFormatSetSerializer


class ProductSizeSerializer(FlexFieldsModelSerializer):
    size = serializers.SerializerMethodField('size_define')
    length = serializers.DecimalField(
        write_only=True,
        max_digits=10, decimal_places=2
    )
    width = serializers.DecimalField(
        write_only=True,
        max_digits=10, decimal_places=2
    )
    height = serializers.DecimalField(
        write_only=True,
        max_digits=10, decimal_places=2
    )
    format = serializers.PrimaryKeyRelatedField(
        queryset=ProductSizeFormatSet.objects.all(),
        write_only=True
    )
    product = product_key_related_field.related_field()

    def size_define(self, obj):
        return "{}{}x{}{}x{}{}".format(
            obj.length, obj.format,
            obj.width, obj.format,
            obj.height, obj.format,
        )

    class Meta:
        model = ProductSize
        fields = ['id', 'url', 'product', 'length', 'width', 'height', 'format', 'size']
        # expandable_fields = {'product': ProductSerializer, 'format': ProductSizeFormatSetSerializer}
        expandable_fields = {'format': ProductSizeFormatSetSerializer}
