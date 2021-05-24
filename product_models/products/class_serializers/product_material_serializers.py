from rest_flex_fields import FlexFieldsModelSerializer

from product_models.products.class_models.product_material import ProductMaterial
from product_models.products.class_serializers.product_material_set_serializers import ProductMaterialSetSerializer


class ProductMaterialSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = ['id', 'url', 'product', 'material']
        # expandable_fields = {'product': ProductSerializer, 'material': ProductMaterialSetSerializer}
        expandable_fields = {'material': ProductMaterialSetSerializer}
