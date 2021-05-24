from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_utils.pagination import StandardResultsSetPagination

from product_models.products.class_models.product import Product
from product_models.products.class_serializers.product_serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('-id').all()

    pagination_class = StandardResultsSetPagination
    serializer_class = ProductSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # IsAuthenticated
    # authentication_classes = [JWTAuthentication, ]
