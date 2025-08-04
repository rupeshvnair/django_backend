from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JewelryItemViewSet


router = DefaultRouter()
router.register(r'jewelry',JewelryItemViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

from django.urls import path
from .views import cors_test_view

urlpatterns = [
    path("cors-test/", cors_test_view),
]
