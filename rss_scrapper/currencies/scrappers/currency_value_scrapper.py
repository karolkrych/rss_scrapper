import datetime
import xml.etree.ElementTree as ET

import requests
from django.db.models import QuerySet

from currencies.models import Currency, CurrencyValueHistory


class CurrencyValueScrapper:
    ENDPOINT_URL_BASE = 'https://www.ecb.europa.eu/rss/fxref-{}.html'

    def get_endpoint_url(self, currency_shortcut: str) -> str:
        return self.ENDPOINT_URL_BASE.format(currency_shortcut.lower())

    def _get_latest_value(self, currency_shortcut: str) -> float:
        page = requests.get(self.get_endpoint_url(currency_shortcut))
        root = ET.fromstring(page.content)
        return float(root[1][5][2][0].text)

    def _create_new_currency_value(self, currency) -> None:
        value = self._get_latest_value(currency.shortcut)
        CurrencyValueHistory.objects.get_or_create(
            currency=currency,
            date_created=datetime.date.today(),
            value=value
        )

    def create_new_currency_values(self) -> None:
        for currency in self._get_currencies():
            self._create_new_currency_value(currency)

    @staticmethod
    def _get_currencies() -> QuerySet:
        return Currency.objects.all()
