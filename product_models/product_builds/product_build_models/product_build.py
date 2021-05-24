from datetime_utils.date_time import DateTime
from django.db import models


# from pcr_models.products.product_builds.product_build_models.product_build_stock import ProductBuildStock


class ProductBuild(models.Model):
    note = models.TextField(blank=True, null=True)
    ordered_date = models.DateField(default=DateTime.datenow)
    required_date = models.DateField(null=True, blank=True)
    finished_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Product builds'
        verbose_name_plural = 'Product builds'

    # def test(self, *args, **kwargs):
    #     if args:
    #         print("args: {}".format(args))
    #     if 'test' in kwargs:
    #         print("kwargs: {}".format(kwargs))
    # 
    # def save(self, *args, **kwargs):
    #     self.test("test", test="test")
    #     super(ProductBuild, self).save(*args, **kwargs)

    def __str__(self):
        return "{} (id:{})".format(self.ordered_date, self.id)
