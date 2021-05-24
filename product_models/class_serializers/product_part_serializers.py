from rest_flex_fields import FlexFieldsModelSerializer

from product_models.class_models.product_part import ProductPart
from product_models.class_serializers.product_serializers import ProductSerializer


class ProductPartSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductPart
        fields = ['id', 'url', 'product', 'part', 'quantity']
        expandable_fields = {'product': ProductSerializer}
