from django.contrib import admin

from product_models.class_models.product_material import ProductMaterialSet, ProductMaterial


class ProductMaterialSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'material', ]
    list_display_links = ['material', ]
    list_per_page = 25


admin.site.register(ProductMaterialSet, ProductMaterialSetAdmin)


# class ProductMaterialAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product', 'material']
#     list_display_links = ['product']
#     list_per_page = 25
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
# admin.site.register(ProductMaterial, ProductMaterialAdmin)


class ProductMaterialAdminInline(admin.TabularInline):
    model = ProductMaterial
    extra = 0
