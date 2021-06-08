from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from product_models.class_models.product_price import ProductPrice, ProductCurrency


class ProductCurrencySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductCurrency
        fields = ['id', 'currency', 'name', 'symbol']
        # expandable_fields = {'product': ProductSerializer, 'format': ProductSizeFormatSetSerializer}
        expandable_fields = {}


class ProductPriceSerializer(FlexFieldsModelSerializer):
    currency = serializers.PrimaryKeyRelatedField(
        queryset=ProductCurrency.objects.all(),
        write_only=True
    )

    price = serializers.DecimalField(
        write_only=True,
        max_digits=20,
        decimal_places=2,
        error_messages={'blank': 'INVALID!!11', 'null': 'NULL11!'}
        # style={'input_type': 'password'}
    )

    product_price = serializers.SerializerMethodField('product_price_define')

    def product_price_define(self, obj):
        return "{} {}".format(obj.price, obj.currency.currency)

    class Meta:
        model = ProductPrice
        fields = ['id', 'url', 'product', 'currency', 'price', 'product_price']
        # expandable_fields = {'product': ProductSerializer, 'format': ProductSizeFormatSetSerializer}
        expandable_fields = {'currency': ProductCurrencySerializer}
