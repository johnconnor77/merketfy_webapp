from django.db import models

from core.models.base_classes import MerketfyBase


class HistoricalPrice(MerketfyBase):
    article = models.ForeignKey(
        'Article',
        on_delete=models.PROTECT)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'historical_price'
