from decimal import Decimal

from django.db import models

from product_models.products.class_models.product import Product


class ProductCurrency(models.Model):
    currency = models.CharField(max_length=30)
    name = models.CharField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.currency


class ProductPrice(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_price')
    currency = models.ForeignKey(ProductCurrency, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))

    # class Meta:
    #     unique_together = (('department', 'name'),)

    def __str__(self):
        return "{} {}".format(self.price, self.currency.currency)
