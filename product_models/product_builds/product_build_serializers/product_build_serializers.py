from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from pcr_models.products.product_builds.product_build_models.product_build_stock import ProductBuild
from pcr_models.products.product_builds.product_build_serializers.product_build_worker_serializers import \
    ProductBuildWorkerSerializer
from pcr_models.products.product_supplies.product_supply_serializiers.product_supply_serializers import \
    ProductSupplySerializer
from pcr_models.staffs.staffs.staff_serializers.staff_serializers import StaffSerializer


class ProductBuildSerializer(FlexFieldsModelSerializer):
    added_by = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)
    build_product_supply = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    product_build_worker = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = ProductBuild
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            'note',
            'ordered_date',
            'required_date',
            'finished_date',
            'build_status',
            'added_by',
            'updated_by',
            'build_product_supply',
            'product_build_worker',
        ]
        expandable_fields = {
            'added_by': StaffSerializer,
            'updated_by': StaffSerializer,
            'product_build_worker': (ProductBuildWorkerSerializer, {'many': True}),
            'build_product_supply': (ProductSupplySerializer, {'many': True}),
        }
