from django.db import models

from product_models.products.class_models.product import Product


class ProductSizeFormatSet(models.Model):
    format = models.CharField(max_length=10)

    def __str__(self):
        return self.format


class ProductSize(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_size')
    format = models.ForeignKey(ProductSizeFormatSet, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name
