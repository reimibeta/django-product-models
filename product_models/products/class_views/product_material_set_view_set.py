from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_models.products.class_models.product_material import ProductMaterialSet
from product_models.products.class_serializers.product_material_set_serializers import ProductMaterialSetSerializer


class ProductMaterialSetViewSet(viewsets.ModelViewSet):
    queryset = ProductMaterialSet.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductMaterialSetSerializer
