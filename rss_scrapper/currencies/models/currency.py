from django.db import models


class Currency(models.Model):
    name = models.CharField('Currency full name', max_length=255)
    shortcut = models.CharField('Shortcut', help_text='i.e. USD for Dollar', max_length=255)

    def __str__(self):
        return f'{self.name} ({self.shortcut})'
