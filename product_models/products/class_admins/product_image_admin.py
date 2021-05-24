from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from image_utils.renders.render_image import render_image

# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product', 'thumbnail_image', ]
#     list_display_links = ['product', 'thumbnail_image']
#     list_per_page = 25
#
#     def thumbnail_image(self, obj):
#         return RenderImage.renderHtmlImage(obj.thumbnail.url)
#
#     list_filter = (
#         # for ordinary fields
#         # ('product__name', DropdownFilter),
#         # for choice fields
#         # ('a_choicefield', ChoiceDropdownFilter),
#         # for related fields
#         ('product', RelatedDropdownFilter),
#     )
#
#
# admin.site.register(ProductImage, ProductImageAdmin)
from product_models.products.class_models.product_image import ProductImage


class ProductImageAdminInline(admin.TabularInline):
    model = ProductImage
    extra = 0
