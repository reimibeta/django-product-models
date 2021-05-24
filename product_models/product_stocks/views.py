from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from pcr_models.products.product_stocks.models import ProductStock
from pcr_models.products.product_stocks.serializers import ProductStockSerializer


class ProductStockViewSet(viewsets.ModelViewSet):
    queryset = ProductStock.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductStockSerializer
