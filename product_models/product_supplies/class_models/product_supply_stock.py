from decimal import Decimal
from django.db import models
from django.db.models.signals import pre_save, post_delete, post_save, pre_delete
from django.dispatch import receiver

from wallet_models.wallet_models.wallet import Wallet

from pcr_models.products.product_classes.product_stock_management import product_stock_supply
from pcr_models.products.product_classes.product_account_management import product_account_outlet
from pcr_models.products.product_stocks.models import ProductStock
from pcr_models.products.product_supplies.product_supply_models.product_supply import ProductSupply


class ProductSupplyStock(models.Model):
    account = models.ForeignKey(
        Wallet, on_delete=models.CASCADE
    )
    supply = models.ForeignKey(
        ProductSupply,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='product_supply_stock'
    )
    stock = models.ForeignKey(
        ProductStock,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    quantity = models.IntegerField(default=0)
    price_per_unit = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00)
    )
    is_transferred = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product supply stocks'
        verbose_name_plural = 'Product supply stocks'

    def __str__(self):
        return "{}".format(self.stock)


@receiver(post_save, sender=ProductSupplyStock)
def add(sender, instance, created, **kwargs):
    if created:
        # stock
        product_stock_supply.supply_stock(current_instance=instance)
        # account
        product_account_outlet.outlet_account(
            instance,
            (instance.price_per_unit * instance.quantity)
        )


@receiver(pre_save, sender=ProductSupplyStock)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        old_value = ProductSupplyStock.objects.get(id=instance.id)
        product_stock_supply.update_stock(current_instance=instance, last_instance=old_value)
        # account
        product_account_outlet.update_outlet_account(
            instance, old_value,
            (instance.price_per_unit * instance.quantity),
            (old_value.price_per_unit * old_value.quantity)
        )


@receiver(pre_delete, sender=ProductSupplyStock)
def delete(sender, instance, using, **kwargs):
    # stock
    old_value = ProductSupplyStock.objects.get(id=instance.id)
    product_stock_supply.return_stock(last_instance=old_value)
    # account
    product_account_outlet.refund_outlet_account(
        old_value,
        (old_value.price_per_unit * old_value.quantity)
    )
