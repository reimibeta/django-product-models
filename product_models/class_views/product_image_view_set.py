from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from product_models.class_models.product_image import ProductImage
from product_models.class_serializers.product_image_serializers import ProductImageSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductImageSerializer
