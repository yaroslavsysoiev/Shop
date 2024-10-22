from django.urls import path, include
from rest_framework import routers

from product.views import ProductViewSet

app_name = "product"

router = routers.DefaultRouter()
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
