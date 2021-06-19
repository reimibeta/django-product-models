from decimal import Decimal

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_datetime.datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    created_date = models.DateField(default=datetime.dnow())
    updated_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    # class Meta:
    #     unique_together = (('department', 'name'),)

    def __str__(self):
        return "{}".format(self.name)


@receiver(pre_save, sender=Product)
def update(sender, instance, **kwargs):
    if instance is None:
        pass
    else:
        instance.updated_date = datetime.dnow(str=True)
