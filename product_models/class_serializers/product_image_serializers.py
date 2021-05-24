from rest_flex_fields import FlexFieldsModelSerializer

from product_models.class_models.product_image import ProductImage


class ProductImageSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'url', 'product', 'image', 'thumbnail']
