from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from pcr_models.products.product_builds.product_build_models.product_build_worker import ProductBuildWorker
from pcr_models.products.product_builds.product_build_serializers.product_build_worker_serializers import \
    ProductBuildWorkerSerializer


class ProductBuildWorkerViewSet(viewsets.ModelViewSet):
    queryset = ProductBuildWorker.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductBuildWorkerSerializer
