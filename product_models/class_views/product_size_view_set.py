from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_models.class_models.product_size import ProductSize
from product_models.class_serializers.product_size_serializers import ProductSizeSerializer


class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSizeSerializer
    search_fields = (
        'product__id',
    )
