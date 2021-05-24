from decimal import Decimal
from enum import Enum
from datetime_utils.date_time import DateTime
from django.db import models
from django.db.models.signals import post_delete, pre_save, post_save, pre_delete
from django.dispatch import receiver
from wallet_models.wallet_models.wallet import Wallet
from pcr_models.products.product_builds.product_build_models.product_build import ProductBuild
from pcr_models.products.product_classes.product_account_management import product_account_outlet
from pcr_models.products.product_stocks.models import ProductStock
from pcr_models.products.product_classes.product_stock_management import product_stock_supply


class ProductBuildStatus(Enum):
    INITIATED = "initiated"
    PROGRESS = "progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CLOSED = "closed"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class ProductBuildStock(models.Model):
    build = models.ForeignKey(
        ProductBuild,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='product_build_stock'
    )
    note = models.TextField(blank=True, null=True)
    account = models.ForeignKey(
        Wallet, on_delete=models.CASCADE
    )
    stock = models.ForeignKey(
        ProductStock,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    quantity = models.IntegerField(default=0)
    cost_build_per_unit = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00)
    )
    is_transferred = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=True)
    build_status = models.CharField(
        max_length=255,
        choices=ProductBuildStatus.choices(),
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        super(ProductBuildStock, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.stock)


@receiver(post_save, sender=ProductBuildStock)
def add(sender, instance, created, **kwargs):
    if created:
        # stock
        product_stock_supply.supply_stock(instance)
        # account
        product_account_outlet.outlet_account(
            instance,
            (instance.cost_build_per_unit * instance.quantity)
        )


@receiver(pre_save, sender=ProductBuildStock)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        # stock
        old_value = ProductBuildStock.objects.get(id=instance.id)
        # update stock
        product_stock_supply.update_stock(current_instance=instance, last_instance=old_value)
        # account
        product_account_outlet.update_outlet_account(
            instance, old_value,
            (instance.cost_build_per_unit * instance.quantity),
            (old_value.cost_build_per_unit * old_value.quantity),
        )


@receiver(pre_delete, sender=ProductBuildStock)
def delete(sender, instance, using, **kwargs):
    # print(instance)
    old_value = ProductBuildStock.objects.get(id=instance.id)
    # return stock
    product_stock_supply.return_stock(last_instance=old_value)
    # refund account
    product_account_outlet.refund_outlet_account(
        old_value,
        (old_value.cost_build_per_unit * old_value.quantity)
    )
