from django.urls import include, path
from rest_framework.routers import DefaultRouter

from currencies.views import CurrencyViewSet, CurrencyValueHistoryViewSet

router = DefaultRouter()
router.register('currencies', CurrencyViewSet, basename='currency')
router.register('currencies_values', CurrencyValueHistoryViewSet, basename='currency_value')

urlpatterns = [
    path('', include(router.urls)),
]
