from django.db import models

from product_models.products.class_models.product import Product


class ProductMaterialSet(models.Model):
    material = models.CharField(max_length=200)

    def __str__(self):
        return self.material


class ProductMaterial(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_material')
    material = models.ForeignKey(ProductMaterialSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
