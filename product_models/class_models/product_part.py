from django.db import models

from product_models.class_models.product import Product


class ProductPart(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True,
        related_name='product_part'
    )
    part = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True
    )
    quantity = models.IntegerField(default=0)

    # class Meta:
    #     unique_together = (('department', 'name'),)

    def __str__(self):
        return "{}".format(self.product)
