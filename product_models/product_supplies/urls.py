from django.conf.urls import url
from django.urls import path, include
from product_models.product_supplies import views
from rest_framework import routers

router = routers.DefaultRouter()
""" Product supply api """
router.register('product-supply', views.ProductSupplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-supply-chart', views.ProductSupplyChartView.as_view())
]
