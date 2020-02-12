from django.test import TestCase

from currencies.scrappers import CurrencyScrapper


class CurrencyScrapperTestCase(TestCase):
    def setUp(self) -> None:
        self.scrapper = CurrencyScrapper()

    def test_get_currency_name_and_shortcut(self):
        self.assertEqual(self.scrapper.get_currency_name_and_shortcut('Zloty polski (PLN)'), ('Zloty polski', 'PLN'))
