from django.db import models

from pcr_models.products.product_builds.product_build_models.product_build_stock import ProductBuildStock
from pcr_models.staffs.staff_groups.staff_group_models.staff_worker import StaffWorker


class ProductBuildWorker(models.Model):
    build = models.ForeignKey(
        ProductBuildStock,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='product_build_worker'
    )
    worker = models.ForeignKey(
        StaffWorker,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return "{}".format(self.worker)
