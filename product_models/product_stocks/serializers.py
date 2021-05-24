from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from pcr_models.products.product_stocks.models import ProductStock
from pcr_models.products.products.product_serializers.product_serializers import ProductSerializer


class ProductStockSerializer(FlexFieldsModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductStock
        # exclude = ('removed_by',)
        fields = [
            'id',
            'product',
            'quantity'
        ]
        expandable_fields = {
            'product': ProductSerializer,
        }
