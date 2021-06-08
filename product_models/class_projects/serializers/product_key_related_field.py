from rest_framework import serializers

from product_models.class_models.product import Product


class ProductKeyRelatedField:

    def related_field(self):
        return serializers.PrimaryKeyRelatedField(
            queryset=Product.objects.filter(
                is_active=True
            ),
            write_only=True
        )


product_key_related_field = ProductKeyRelatedField()
