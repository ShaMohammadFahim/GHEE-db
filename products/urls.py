from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductVariantViewSet, UnitViewSet

router = DefaultRouter()
router.register(r'list', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'variants', ProductVariantViewSet)
router.register(r'units', UnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]