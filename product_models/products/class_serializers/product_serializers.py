from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

# url: http://127.0.0.1:8000/api/products/product/?expand=productsize.format,productmaterial.material
from product_models.products.class_models.product import Product
from product_models.products.class_serializers.product_image_serializers import ProductImageSerializer
from product_models.products.class_serializers.product_material_serializers import ProductMaterialSerializer
from product_models.products.class_serializers.product_price_serializers import ProductPriceSerializer
from product_models.products.class_serializers.product_size_serializers import ProductSizeSerializer


class ProductSerializer(FlexFieldsModelSerializer):
    product_size = serializers.PrimaryKeyRelatedField(read_only=True)
    product_material = serializers.PrimaryKeyRelatedField(read_only=True)
    product_image = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    product_part = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    product_price = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    # price = serializers.DecimalField(
    #     write_only=True,
    #     max_digits=20,
    #     decimal_places=2,
    #     error_messages={'blank': 'INVALID!!11', 'null': 'NULL11!'}
    #     # style={'input_type': 'password'}
    # )
    # product_price = serializers.SerializerMethodField('price_unit')
    #
    # def price_unit(self, obj):
    #     return "{} {}".format(obj.price, obj.account.currency.currency)

    class Meta:
        model = Product
        fields = [
            'id',
            'url',
            'name',
            # 'price',
            'product_price',
            'created_date',
            'updated_date',
            'product_size',
            'product_material',
            'product_image',
            'product_part',
        ]
        expandable_fields = {
            'product_size': ProductSizeSerializer,
            'product_material': ProductMaterialSerializer,
            'product_image': (ProductImageSerializer, {'many': True}),
            'product_price': ProductPriceSerializer,
        }
