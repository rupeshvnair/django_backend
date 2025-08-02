from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JewelryItemViewSet


router = DefaultRouter()
router.register(r'items',JewelryItemViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
