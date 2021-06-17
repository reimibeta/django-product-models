from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from product_models.class_models.product_material import ProductMaterialSet
from product_models.class_serializers.product_material_set_serializers import ProductMaterialSetSerializer


class ProductMaterialSetViewSet(viewsets.ModelViewSet):
    queryset = ProductMaterialSet.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductMaterialSetSerializer
