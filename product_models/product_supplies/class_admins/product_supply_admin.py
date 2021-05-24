from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from html_render_utils.html_render import HtmlRender

from product_models.product_supplies.class_admins.product_supply_delivery_admin import ProductSupplyDeliveryAdminInline
from product_models.product_supplies.class_admins.product_supply_stock_admin import ProductSupplyStockAdminInline
from product_models.product_supplies.class_models.product_supply import ProductSupply
from product_models.product_supplies.class_models.product_supply_stock import ProductSupplyStock


class ProductSupplyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'note',
        'products',
        'supplier',
        'request_date',
        'supply_date',
    )
    list_display_links = ['note', 'supplier', 'products', ]
    # list_editable = []
    list_per_page = 25

    # readonly_fields = ['staff', ]
    def products(self, obj):
        arr = []
        stocks = ProductSupplyStock.objects.filter(supply=obj.id).all()
        if stocks:
            i = 0
            for stock in stocks:
                i = i + 1
                transfer = "transferred" if stock.is_transferred else "not transfer"
                paid = "paid" if stock.is_paid else "not paid"
                arr.append("{}-{}({})({})({})".format(
                    i, stock.stock,
                    stock.quantity,
                    transfer,
                    paid
                ))
        return HtmlRender.p(HtmlRender.br().join(arr), '#10284e')

    list_filter = (
        # for ordinary fields
        ('request_date', DropdownFilter),
        ('supply_date', DropdownFilter),
        ('product_supply_stock__is_paid', DropdownFilter),
        ('product_supply_stock__is_transferred', DropdownFilter),
        # for choice fields
        ('product_supply_stock__stock__product__name', DropdownFilter),
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('supplier', RelatedDropdownFilter),
    )
    # ordering = ['-supply_date']
    inlines = [
        ProductSupplyStockAdminInline,
        ProductSupplyDeliveryAdminInline,
    ]
    search_fields = [
        'product_supply_stock__stock__product__name'
    ]


admin.site.register(ProductSupply, ProductSupplyAdmin)
