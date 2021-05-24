from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_models.products.class_models.product_price import ProductPrice
from product_models.products.class_serializers.product_price_serializers import ProductPriceSerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductPriceSerializer
    search_fields = (
        'product__id',
    )
