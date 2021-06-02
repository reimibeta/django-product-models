from rest_flex_fields import FlexFieldsModelSerializer

from product_models.class_models.product_size import ProductSize
from product_models.class_serializers.product_size_format_set_serializers import \
    ProductSizeFormatSetSerializer


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id', 'url', 'product', 'length', 'width', 'height', 'format']
        # expandable_fields = {'product': ProductSerializer, 'format': ProductSizeFormatSetSerializer}
        expandable_fields = {'format': ProductSizeFormatSetSerializer}
