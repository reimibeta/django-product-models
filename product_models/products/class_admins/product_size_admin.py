from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

from product_models.products.class_models.product_size import ProductSizeFormatSet, ProductSize


class ProductSizeFormatSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'format', ]
    list_display_links = ['format', ]
    list_per_page = 25


admin.site.register(ProductSizeFormatSet, ProductSizeFormatSetAdmin)


# class ProductSizeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product', 'length_size', 'width_size', 'height_size')
#     list_display_links = ['product', ]
#     list_per_page = 25
#
#     def length_size(self, obj):
#         return "{}{}".format(obj.length, obj.format)
#
#     def width_size(self, obj):
#         return "{}{}".format(obj.width, obj.format)
#
#     def height_size(self, obj):
#         return "{}{}".format(obj.height, obj.format)
#
#     list_filter = (
#         # for ordinary fields
#         ('product__name', DropdownFilter),
#         # for choice fields
#         # ('a_choicefield', ChoiceDropdownFilter),
#         # for related fields
#         # ('user', RelatedDropdownFilter),
#     )
#
#
# admin.site.register(ProductSize, ProductSizeAdmin)


class ProductSizeAdminInline(admin.TabularInline):
    model = ProductSize
    extra = 0
