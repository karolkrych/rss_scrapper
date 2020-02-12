from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from currencies.models import CurrencyValueHistory


class CurrencyValueHistorySerializer(ModelSerializer):
    currency_name = SerializerMethodField()

    class Meta:
        model = CurrencyValueHistory
        fields = '__all__'

    def get_currency_name(self, obj):
        return obj.currency.name
