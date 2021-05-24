from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from image_utils.renders.render_image import render_image

from product_models.products.class_models.product_image import ProductImage
from product_models.products.class_models.product_price import ProductCurrency, ProductPrice


class ProductCurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'currency', 'name', 'symbol']
    list_display_links = ['currency']
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('currency', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('currency', RelatedDropdownFilter),
    )


admin.site.register(ProductCurrency, ProductCurrencyAdmin)


class ProductPriceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_image',
        'product',
        'product_price',
    ]
    list_display_links = ['product', 'product_image', ]
    list_per_page = 25
    search_fields = [
        'product'
    ]

    def product_price(self, obj):
        if obj.currency is not None:
            return "{} {}".format(obj.price, obj.currency.currency)
        else:
            return "not provided"

    def product_image(self, obj):
        image = ProductImage.objects.filter(product=obj.product.id).first()
        return render_image.render(image.thumbnail.url) if image is not None else "Not provide"

    list_filter = (
        # for ordinary fields
        ('product__name', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('product', RelatedDropdownFilter),
    )

    inlines = []


admin.site.register(ProductPrice, ProductPriceAdmin)


class ProductPriceAdminInline(admin.TabularInline):
    model = ProductPrice
    extra = 0
