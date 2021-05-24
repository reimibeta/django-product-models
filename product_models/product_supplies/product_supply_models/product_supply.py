from datetime_utils.date_time import DateTime
from django.db import models

from pcr_models.suppliers.suppliers.models import Supplier


class ProductSupply(models.Model):
    note = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    request_date = models.DateField(default=DateTime.datenow)
    supply_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Product supplies'
        verbose_name_plural = 'Product supplies'

    def __str__(self):
        return "{} (id:{})".format(self.supplier, self.id)
