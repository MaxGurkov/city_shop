from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, StreetViewSet, ShopViewSet

router = DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'street', StreetViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
