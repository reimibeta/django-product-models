from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from product_models.class_models.product_price import ProductPrice
from product_models.class_serializers.product_price_serializers import ProductPriceSerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductPriceSerializer
    search_fields = (
        'product__id',
    )
