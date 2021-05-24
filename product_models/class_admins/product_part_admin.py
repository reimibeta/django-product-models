from django.contrib import admin
from product_models.class_models.product_part import ProductPart


# class ProductPartAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product', 'part')
#     list_display_links = ['product', ]
#     list_per_page = 25
#
#     list_filter = (
#         # for ordinary fields
#         ('product__name', DropdownFilter),
#         ('part__name', DropdownFilter),
#         # for choice fields
#         # ('a_choicefield', ChoiceDropdownFilter),
#         # for related fields
#         # ('user', RelatedDropdownFilter),
#     )
#
#
# admin.site.register(ProductPart, ProductPartAdmin)


class ProductPartAdminInline(admin.TabularInline):
    model = ProductPart
    extra = 0
    fk_name = "product"
