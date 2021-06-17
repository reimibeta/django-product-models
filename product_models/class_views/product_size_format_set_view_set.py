from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from product_models.class_models.product_size import ProductSizeFormatSet
from product_models.class_serializers.product_size_format_set_serializers import ProductSizeFormatSetSerializer


class ProductSizeFormatSetViewSet(viewsets.ModelViewSet):
    queryset = ProductSizeFormatSet.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSizeFormatSetSerializer
