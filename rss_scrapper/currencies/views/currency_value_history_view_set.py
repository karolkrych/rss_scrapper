from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from currencies.models import CurrencyValueHistory
from currencies.serializers import CurrencyValueHistorySerializer


class CurrencyValueHistoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CurrencyValueHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['currency', ]

    def get_queryset(self):
        return CurrencyValueHistory.objects.all()
