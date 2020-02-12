import re

import requests
from bs4 import BeautifulSoup

from currencies.models import Currency


class CurrencyScrapper:
    ENDPOINT_URL = 'https://www.ecb.europa.eu/home/html/rss.en.html'

    @staticmethod
    def _create_currency(name, shortcut: str) -> None:
        Currency.objects.get_or_create(name=name, shortcut=shortcut)

    def create_currencies(self) -> None:
        for currency in self._get_currencies_data():
            name, shortcut = self._get_currency_name_and_shortcut(currency.text)
            self._create_currency(name=name, shortcut=shortcut)

    def _get_currencies_data(self) -> list:
        page = requests.get(self.ENDPOINT_URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        currencies = soup.findAll("a", {"class": "rss"})[10:]
        return currencies[:-1]

    @staticmethod
    def _get_currency_name_and_shortcut(value) -> (str, str):
        shortcut = re.findall(r'\(.*?\)', value)[0][1:][:-1]
        name = value.replace(f' ({shortcut})', '')
        return name, shortcut
