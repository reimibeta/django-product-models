from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from pcr_models.products.product_builds.product_build_models.product_build_worker import ProductBuildWorker
from pcr_models.staffs.staff_groups.staff_group_serializers.staff_worker_serializers import StaffWorkerSerializer


class ProductBuildWorkerSerializer(FlexFieldsModelSerializer):
    # worker = serializers.PrimaryKeyRelatedField(read_only=True)
    # order = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductBuildWorker
        fields = [
            'id',
            'url',
            'build',
            'worker'
        ]
        expandable_fields = {
            'worker': StaffWorkerSerializer,
        }
