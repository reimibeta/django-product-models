from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from pcr_models.products.product_builds.product_build_admins.product_build_worker_admin import \
    ProductBuildWorkerAdminInline
from html_render_utils.html_render import HtmlRender

from pcr_models.products.product_builds.product_build_models.product_build_stock import ProductBuildStock
from pcr_models.products.product_stocks.models import ProductStock

""" product build """


class ProductBuildStockAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'note',
        'stock',
        'build',
        # 'supplier',
        # 'quantity',
        'status',
        'is_transferred',
        'is_paid',
        # 'ordered_date',
        # 'required_date',
        # 'added_by',
        # 'updated_by',
    ]
    list_display_links = [
        'id',
        'note',
        'stock',
        'build',
    ]
    list_per_page = 25

    # readonly_fields = ['added_by', 'updated_by']

    search_fields = [
        'stock__product__name'
    ]

    list_filter = (
        # for ordinary fields
        # ('ordered_date', DropdownFilter),
        # ('is_finished', DropdownFilter),
        # for choice fields
        ('build_status', ChoiceDropdownFilter),
        # for related fields
        # ('supplier', RelatedDropdownFilter),
    )

    inlines = [
        # ProductSupplyStockAdminInline,
        ProductBuildWorkerAdminInline,
    ]

    def status(self, obj):
        print(obj.build_status)
        if obj.build_status == "COMPLETED":
            return HtmlRender.p(obj.build_status, "green")
        elif obj.build_status == "PROGRESS":
            return HtmlRender.p(obj.build_status, "orange")
        else:
            return obj.build_status

    def stocks(self, obj):
        arr = []
        builds = ProductBuildStock.objects.filter(id=obj.id)
        if builds:
            i = 0
            for build in builds:
                i = i + 1
                transfer = "transferred" if build.is_transferred else "not transfer"
                arr.append("{}-{}({})({})".format(
                    i,
                    build.stock,
                    build.quantity,
                    transfer
                ))
        return HtmlRender.p(HtmlRender.br().join(arr), '#10284e')

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
    # def save_model(self, request, obj, form, change):
    #
    #     # added by staff
    #     staff = Staff.objects.filter(user=request.user).last()
    #     if staff:
    #         # create
    #         if not change:
    #             obj.added_by = staff
    #         else:
    #             # update
    #             obj.updated_by = staff
    #
    #     obj.save()


admin.site.register(ProductBuildStock, ProductBuildStockAdmin)


class ProductBuildStockAdminInline(admin.StackedInline):
    model = ProductBuildStock
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
