from django.contrib import admin

from .models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    class Meta:
        model = Currency
    properties = ["currency", 'source', 'buy', 'sell', 'created', 'updated']


admin.site.register(Currency, CurrencyAdmin)
