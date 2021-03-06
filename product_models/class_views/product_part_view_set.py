from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from product_models.class_models.product_part import ProductPart
from product_models.class_serializers.product_part_serializers import ProductPartSerializer


class ProductPartViewSet(viewsets.ModelViewSet):
    queryset = ProductPart.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductPartSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            print('login')
        else:
            print('not login')
        if 'product' in self.request.GET:
            product = self.request.GET['product']
            # print(product)
            if not product:
                print('not request')
                return qs
            elif product == 'ALL':
                return qs
            else:
                components = ProductPart.objects.filter(product=product)
                return components
        else:
            return qs
