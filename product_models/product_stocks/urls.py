from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from pcr_models.products.product_stocks import views

router = routers.DefaultRouter()
""" Product stock api """
router.register('product-stock', views.ProductStockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
