from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from image_utils.renders.render_image import render_image

from pcr_models.products.product_stocks.models import ProductStock
from pcr_models.products.products.product_models.product import Product
from pcr_models.products.products.product_models.product_image import ProductImage


class ProductStockAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_image', 'product', 'quantity', 'is_available')
    list_display_links = ['product', 'product_image', ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        ('quantity', DropdownFilter),
        ('is_available', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('product', RelatedDropdownFilter),
    )
    search_fields = [
        'product__name'
    ]

    def product_image(self, obj):
        image = ProductImage.objects.filter(product=obj.product).first()
        if image:
            return render_image.render(image.thumbnail.url)
        else:
            return "Not provide"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # stock
        if db_field.name == "product":
            try:
                # parent_id = request.resolver_match.args[0]
                kwargs["queryset"] = Product.objects.filter(
                    is_active=True
                ).order_by('name')
            except IndexError:
                pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(ProductStock, ProductStockAdmin)


class ProductStockAdminInline(admin.TabularInline):
    model = ProductStock
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # stock
        if db_field.name == "stock":
            try:
                # parent_id = request.resolver_match.args[0]
                kwargs["queryset"] = Product.objects.filter(
                    is_available=True
                ).order_by('name')
            except IndexError:
                pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
