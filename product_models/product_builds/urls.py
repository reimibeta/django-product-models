from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from pcr_models.products.product_builds import views

router = routers.DefaultRouter()
""" product build api """
router.register('product-build', views.ProductBuildViewSet)

""" product build worker api """
router.register('product-build-worker', views.ProductBuildWorkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
