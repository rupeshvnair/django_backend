from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JewelryItemViewSet


router = DefaultRouter()
router.register(r'jewelry',JewelryItemViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
