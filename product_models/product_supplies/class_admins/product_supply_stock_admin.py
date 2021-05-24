from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from product_models.product_stocks.models import ProductStock
from product_models.product_supplies.class_models.product_supply_stock import ProductSupplyStock


class ProductSupplyStockAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'supply',
        'stock',
        'quantity',
        'supply_price_per_unit',
        'supply_price_total',
        'is_transferred'
    )
    list_display_links = ['supply', 'stock', ]
    list_editable = [
        # 'quantity',
        'is_transferred',
    ]
    list_per_page = 25

    # readonly_fields = ['staff', ]
    # exclude = ['build', ]

    list_filter = (
        # for ordinary fields
        ('quantity', DropdownFilter),
        ('price_per_unit', DropdownFilter),
        ('is_transferred', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('supply', RelatedDropdownFilter),
        ('stock', RelatedDropdownFilter),
    )
    inlines = []

    search_fields = [
        'stock__product__name'
    ]

    def supply_price_per_unit(self, obj):
        return "{} {}".format(obj.price_per_unit, obj.account.currency.currency)

    def supply_price_total(self, obj):
        return "{} {}".format(
            obj.price_per_unit * obj.quantity, obj.account.currency.currency
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # stock
        if db_field.name == "stock":
            try:
                # parent_id = request.resolver_match.args[0]
                kwargs["queryset"] = ProductStock.objects.filter(
                    is_available=True
                ).order_by('product__name')
            except IndexError:
                pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(ProductSupplyStock, ProductSupplyStockAdmin)


class ProductSupplyStockAdminInline(admin.TabularInline):
    model = ProductSupplyStock
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # stock
        if db_field.name == "stock":
            try:
                # parent_id = request.resolver_match.args[0]
                kwargs["queryset"] = ProductStock.objects.filter(
                    is_available=True
                ).order_by('product__name')
            except IndexError:
                pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
