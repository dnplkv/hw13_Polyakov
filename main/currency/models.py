from django.db import models
from django.utils.timezone import now


class Currency(models.Model):
    select_currency = (
        (1, 'USD'),
        (2, 'EUR'),
    )
    select_resource = (
        (1, 'MONOBANK'),
        (2, 'VKURSE'),
        (3, 'YAHOO'),
    )
    currency = models.PositiveSmallIntegerField(choices=select_currency)
    source = models.PositiveSmallIntegerField(choices=select_resource)
    buy = models.DecimalField(max_digits=6, decimal_places=3)
    sell = models.DecimalField(max_digits=6, decimal_places=3)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(default=now)

    def __str__(self):
        return str({
            'currency': self.currency,
            'source': self.source,
            'buy': self.buy,
            'sell': self.sell,
            'created': self.created,
            'updated': self.updated
        })
