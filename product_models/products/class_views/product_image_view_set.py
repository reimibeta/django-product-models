from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_models.products.class_models.product_image import ProductImage
from product_models.products.class_serializers.product_image_serializers import ProductImageSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductImageSerializer
