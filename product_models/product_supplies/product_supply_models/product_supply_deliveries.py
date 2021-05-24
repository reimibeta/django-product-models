from decimal import Decimal
from enum import Enum

from datetime_utils.date_time import DateTime
from django.db import models

# delivery choice
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver

from wallet_models.wallet_models.wallet import Wallet

from pcr_models.classes.balances.outlets.balance_outlet import BalanceOutlet
from pcr_models.products.product_supplies.product_supply_models.product_supply import ProductSupply
from pcr_models.staffs.staff_groups.staff_group_models.staff_deliver import StaffDeliver
from pcr_models.classes.balances.outlets.balance_outlet_condition import balance_outlet_condition


class DeliveryStatusChoice(Enum):
    UNFULFILLED = "unfulfilled"
    DELIVERING = "delivering"
    RETURNING = "returning"
    ARRIVED = "arrived"
    COLLECTED = "collected"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


# payment choice
class PaymentStatusChoice(Enum):
    OPTIONAL = "optional"
    EXPIRED = "expired"
    REFUND = "refund"
    FAILED = "failed"
    UNPAID = "unpaid"
    PAID = "paid"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ProductSupplyDelivery(models.Model):
    account = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    supply = models.ForeignKey(
        ProductSupply,
        on_delete=models.CASCADE,
        related_name='product_supply_deliveries',
        blank=True,
        null=True
    )
    deliver = models.ForeignKey(StaffDeliver, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cost_delivery = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    delivery_date = models.DateTimeField(default=DateTime.datetimenow)
    arrived_date = models.DateTimeField(null=True, blank=True)
    payment_status = models.CharField(
        choices=PaymentStatusChoice.choices(),
        blank=True,
        null=True,
        max_length=120
    )

    delivery_status = models.CharField(
        choices=DeliveryStatusChoice.choices(),
        blank=True,
        null=True,
        max_length=120
    )

    class Meta:
        verbose_name = 'Product supply deliveries'
        verbose_name_plural = 'Product supply deliveries'

    def save(self, *args, **kwargs):
        super(ProductSupplyDelivery, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.deliver)


@receiver(post_save, sender=ProductSupplyDelivery)
def add(sender, instance, created, **kwargs):
    if created:
        # account
        balance_outlet_condition.set_current_condition((instance.payment_status == PaymentStatusChoice.PAID.name))
        balance_outlet_condition.current_pk(instance.account.id)
        balance_outlet_condition.outlet_account(instance.cost_delivery)


@receiver(pre_save, sender=ProductSupplyDelivery)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        old_value = ProductSupplyDelivery.objects.get(id=instance.id)
        # account
        balance_outlet_condition.set_current_condition((instance.payment_status == PaymentStatusChoice.PAID.name))
        balance_outlet_condition.current_pk(instance.account.id)
        balance_outlet_condition.set_last_condition((old_value.payment_status == PaymentStatusChoice.PAID.name))
        balance_outlet_condition.last_pk(old_value.account.id)
        balance_outlet_condition.update_outlet_account(instance.cost_delivery, old_value.cost_delivery)


@receiver(pre_delete, sender=ProductSupplyDelivery)
def delete(sender, instance, using, **kwargs):
    old_value = ProductSupplyDelivery.objects.get(id=instance.id)
    # account
    balance_outlet_condition.set_last_condition(old_value.payment_status == PaymentStatusChoice.PAID.name)
    balance_outlet_condition.set_last_pk(old_value.account.id)
    balance_outlet_condition.refund_outlet_account(last_amount=old_value.cost_delivery)
    # if old_value.payment_status == PaymentStatusChoice.PAID.name:
    #     BalanceOutlet.refund(old_value.cost_delivery, old_value.account.id)
