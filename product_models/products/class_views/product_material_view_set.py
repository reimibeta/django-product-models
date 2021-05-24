from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_models.products.class_models.product_material import ProductMaterial
from product_models.products.class_serializers.product_material_serializers import ProductMaterialSerializer


class ProductMaterialViewSet(viewsets.ModelViewSet):
    queryset = ProductMaterial.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductMaterialSerializer
