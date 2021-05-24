from uuid import uuid4

from django.db import models
from image_utils.compress.compress_image import compress_image

from product_models.products.class_models.product import Product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='images/products/', null=True)
    thumbnail = models.ImageField(
        upload_to='images/products/thumbnails/',
        blank=True, null=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        if str(self.image.path) == str(self.image.file):
            print('return true when on new file uploaded!')
        else:
            self.image = compress_image.resize(self.image, 900)
            self.thumbnail = compress_image.resize(self.image, 500)
        super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.image.url
