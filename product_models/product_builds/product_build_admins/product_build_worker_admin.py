
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from pcr_models.products.product_builds.product_build_models.product_build_worker import ProductBuildWorker
from pcr_models.staffs.staff_groups.staff_group_models.staff_worker import StaffWorker


# class ProductBuildWorkerAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'build',
#         'worker'
#     ]
#     list_display_links = ['build', 'worker']
#     list_per_page = 25
#     list_filter = (
#         ('build', RelatedDropdownFilter),
#         ('worker', RelatedDropdownFilter),
#     )
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "worker":
#             # db_field['customer']
#             kwargs["queryset"] = StaffWorker.objects.filter(is_active=True).all()
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#
#
# admin.site.register(ProductBuildWorker, ProductBuildWorkerAdmin)


class ProductBuildWorkerAdminInline(admin.TabularInline):
    model = ProductBuildWorker
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "worker":
            # db_field['customer']
            kwargs["queryset"] = StaffWorker.objects.filter(is_active=True).all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
