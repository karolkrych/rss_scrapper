from django.db import models

from currencies.models import Currency


class CurrencyValueHistory(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    value = models.FloatField()
