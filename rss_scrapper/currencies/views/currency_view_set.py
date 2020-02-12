from rest_framework.viewsets import ReadOnlyModelViewSet

from currencies.models import Currency
from currencies.serializers import CurrencySerializer


class CurrencyViewSet(ReadOnlyModelViewSet):
    serializer_class = CurrencySerializer

    def get_queryset(self):
        return Currency.objects.all()
