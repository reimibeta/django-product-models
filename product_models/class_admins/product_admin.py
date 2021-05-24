from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from image_utils.renders.render_image import render_image

from product_models.class_admins.product_image_admin import ProductImageAdminInline
from product_models.class_admins.product_material_admin import ProductMaterialAdminInline
from product_models.class_admins.product_part_admin import ProductPartAdminInline
from product_models.class_admins.product_price_admin import ProductPriceAdminInline
from product_models.class_admins.product_size_admin import ProductSizeAdminInline
from product_models.class_models.product import Product
from product_models.class_models.product_image import ProductImage
from product_models.class_models.product_size import ProductSize


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_image',
        'name',
        'product_price',
        'product_material',
        'size',
        'is_active'
    ]
    list_display_links = ['name', 'product_image', ]
    list_per_page = 25
    search_fields = [
        'name'
    ]

    # def product_price(self, obj):
    #     if obj.account.currency is not None:
    #         return "{} {}".format(obj.price, obj.account.currency.currency)
    #     else:
    #         return "not provided"

    # readonly_fields = ['quantity', ]
    # def isActive(self, obj):
    #     check = 'available' if obj.available else 'not available'
    #     color = 'green' if obj.available else 'orange'
    #     return HtmlRender.p(text=check, color=color)

    def size(self, obj):
        size = ProductSize.objects.filter(product=obj.id).first()
        return "{}{}*{}{}*{}{}".format(
            size.length, size.format, size.width, size.format, size.height, size.format
        ) if size is not None else "Not provide"

    def product_image(self, obj):
        image = ProductImage.objects.filter(product=obj.id).first()
        return render_image.render(image.thumbnail.url) if image is not None else "Not provide"

    list_filter = (
        # for ordinary fields
        ('name', DropdownFilter),
        # ('available', DropdownFilter),
        ('product_size__length', DropdownFilter),
        ('product_size__width', DropdownFilter),
        ('product_size__height', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('product_material__material', RelatedDropdownFilter),
    )

    inlines = [
        ProductPriceAdminInline,
        ProductMaterialAdminInline,
        ProductSizeAdminInline,
        ProductImageAdminInline,
        ProductPartAdminInline
    ]


admin.site.register(Product, ProductAdmin)
