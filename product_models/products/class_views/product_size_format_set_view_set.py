from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_models.products.class_models.product_size import ProductSizeFormatSet
from product_models.products.class_serializers.product_size_format_set_serializers import ProductSizeFormatSetSerializer


class ProductSizeFormatSetViewSet(viewsets.ModelViewSet):
    queryset = ProductSizeFormatSet.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSizeFormatSetSerializer
