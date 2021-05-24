from django.urls import path, include
from product_models import views
from rest_framework import routers

router = routers.DefaultRouter()
""" Product Build api """
router.register('product', views.ProductViewSet)
router.register('product-size', views.ProductSizeViewSet)
router.register('product-size-format', views.ProductSizeFormatSetViewSet)
router.register('product-image', views.ProductImageViewSet)
router.register('product-material', views.ProductMaterialViewSet)
router.register('product-material-set', views.ProductMaterialSetViewSet)
router.register('product-part', views.ProductPartViewSet)
router.register('product-price', views.ProductPriceViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
