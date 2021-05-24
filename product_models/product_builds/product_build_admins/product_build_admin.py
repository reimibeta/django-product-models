from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from pcr_models.products.product_builds.product_build_admins.product_build_stock_admin import \
    ProductBuildStockAdminInline
from pcr_models.products.product_builds.product_build_admins.product_build_worker_admin import \
    ProductBuildWorkerAdminInline
from html_render_utils.html_render import HtmlRender

from pcr_models.products.product_builds.product_build_models.product_build import ProductBuild
from pcr_models.products.product_builds.product_build_models.product_build_stock import ProductBuildStock

""" product build """


class ProductBuildAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'note',
        'stocks',
        'ordered_date',
        'required_date',
        'finished_date',
        # 'added_by',
        # 'updated_by',
    ]
    list_display_links = [
        'id',
        'note',
        'stocks',
        'ordered_date',
    ]
    list_per_page = 25

    # readonly_fields = ['added_by', 'updated_by']

    search_fields = [
        'product_build_stock__stock__product__name'
    ]

    list_filter = (
        # for ordinary fields
        ('ordered_date', DropdownFilter),
        ('product_build_stock__is_paid', DropdownFilter),
        ('product_build_stock__is_transferred', DropdownFilter),
        # for choice fields
        ('product_build_stock__stock__product__name', DropdownFilter),
        ('product_build_stock__build_status', ChoiceDropdownFilter),
        # for related fields
        # ('supplier', RelatedDropdownFilter),
    )
    # ordering = ['-required_date']
    inlines = [
        # ProductSupplyStockAdminInline,
        # ProductBuildWorkerAdminInline,
        ProductBuildStockAdminInline,
    ]

    # def status(self, obj):
    #     print(obj.build_status)
    #     if obj.build_status == "COMPLETED":
    #         return HtmlRender.p(obj.build_status, "green")
    #     elif obj.build_status == "PROGRESS":
    #         return HtmlRender.p(obj.build_status, "orange")
    #     else:
    #         return obj.build_status

    def stocks(self, obj):
        arr = []
        builds = ProductBuildStock.objects.filter(build=obj.id)
        if builds:
            i = 0
            for build in builds:
                i = i + 1
                transfer = "transferred" if build.is_transferred else "not transfer"
                paid = "paid" if build.is_paid else "not paid"
                arr.append("{}-{}({})({})({})".format(
                    i,
                    build.stock,
                    build.quantity,
                    transfer,
                    paid
                ))
        return HtmlRender.p(HtmlRender.br().join(arr), '#10284e')

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


admin.site.register(ProductBuild, ProductBuildAdmin)
