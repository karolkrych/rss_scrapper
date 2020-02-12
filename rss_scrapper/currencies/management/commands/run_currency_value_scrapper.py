from django.core.management.base import BaseCommand

from currencies.scrappers import CurrencyValueScrapper


class Command(BaseCommand):
    help = 'Runs scrapper which retrieves exchange rates'

    def handle(self, *args, **options):
        scrapper = CurrencyValueScrapper()
        scrapper.create_new_currency_values()
