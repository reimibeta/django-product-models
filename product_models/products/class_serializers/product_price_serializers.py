from rest_flex_fields import FlexFieldsModelSerializer

from product_models.products.class_models.product_price import ProductPrice, ProductCurrency


class ProductCurrencySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductCurrency
        fields = ['id', 'currency', 'name', 'symbol']
        # expandable_fields = {'product': ProductSerializer, 'format': ProductSizeFormatSetSerializer}
        expandable_fields = {}


class ProductPriceSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['id', 'url', 'product', 'currency', 'price']
        # expandable_fields = {'product': ProductSerializer, 'format': ProductSizeFormatSetSerializer}
        expandable_fields = {'currency': ProductCurrencySerializer}
