from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from pcr_models.products.product_supplies.product_supply_models.product_supply_deliveries import ProductSupplyDelivery
from pcr_models.staffs.staff_groups.staff_group_models.staff_deliver import StaffDeliver


class ProductSupplyDeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'account',
        'supply',
        'deliver',
        'quantity',
        'delivery_price',
        'delivery_date',
        'arrived_date',
    )
    ist_display_links = ['deliver', ]
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('delivery_date', DropdownFilter),
        ('arrived_date', DropdownFilter),
        ('quantity', DropdownFilter),
        # for choice fields
        # ('delivery_status', ChoiceDropdownFilter),
        # for related fields
        ('supply', RelatedDropdownFilter),
        ('deliver', RelatedDropdownFilter),
    )

    def delivery_price(self, obj):
        if obj.account.currency is not None:
            return "{} {}".format(obj.cost_delivery, obj.account.currency.currency)
        else:
            return "not provided"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "deliver":
            # db_field['customer']
            kwargs["queryset"] = StaffDeliver.objects.filter(is_active=True).all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(ProductSupplyDelivery, ProductSupplyDeliveryAdmin)


class ProductSupplyDeliveryAdminInline(admin.StackedInline):
    model = ProductSupplyDelivery
    extra = 0
