from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from product_models.class_models.product_size import ProductSize
from product_models.class_serializers.product_size_serializers import ProductSizeSerializer


class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSizeSerializer
    search_fields = (
        'product__id',
    )
