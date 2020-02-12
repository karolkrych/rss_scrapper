from django.test import TestCase

from currencies.models import CurrencyValueHistory
from currencies.scrappers import CurrencyValueScrapper


class CurrencyValueScrapperTestCase(TestCase):
    def setUp(self) -> None:
        self.scrapper = CurrencyValueScrapper()

    def test_get_endpoint_url(self):
        self.assertEqual(self.scrapper.get_endpoint_url('usd'), 'https://www.ecb.europa.eu/rss/fxref-usd.html')

    def test_saving_new_currency_values(self):
        self.assertEqual(CurrencyValueHistory.objects.all().count(), 0)
        self.scrapper.create_new_currency_values()
        self.assertNotEqual(CurrencyValueHistory.objects.all().count(), 0)
