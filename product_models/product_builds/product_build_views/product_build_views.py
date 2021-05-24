from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_utils.pagination import StandardResultsSetPagination

from pcr_models.products.product_builds.product_build_models.product_build_stock import ProductBuild
from pcr_models.products.product_builds.product_build_serializers.product_build_serializers import \
    ProductBuildSerializer
from pcr_models.staffs.staffs.staff_models.staff import Staff


class ProductBuildViewSet(viewsets.ModelViewSet):
    queryset = ProductBuild.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductBuildSerializer

    # permission_classes = (permissions.IsAuthenticated,)  # IsAuthenticated, IsAuthenticatedOrReadOnly
    # authentication_classes = [JWTAuthentication, ]

    def create(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            staff = Staff.objects.filter(user=self.request.user).first()
            if staff:
                request.data._mutable = True
                request.data['added_by'] = staff.id
                request.data._mutable = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # update
    def update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        if self.request.user.is_authenticated:
            staff = Staff.objects.filter(user=self.request.user).first()
            if staff:
                print("update updated_by")
                request.data._mutable = True
                request.data['updated_by'] = staff.id
                request.data._mutable = False
        serializer = self.serializer_class(instance, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            print('login')
        else:
            print('not login')
        if 'build_status' in self.request.GET:
            request = self.request.GET['build_status']
            if request == "all":
                return qs
            else:
                status = 'COMPLETED' if request == 'COMPLETED' else 'PROGRESS'
                orders = ProductBuild.objects.order_by('-id') \
                    .filter(build_status=status)
                return orders
        else:
            return qs
