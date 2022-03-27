from django.db import models

from core.models.base_classes import MerketfyBase


class Alert(MerketfyBase):
    article = models.ForeignKey(
        'Article',
        on_delete=models.PROTECT)
    persons = models.ManyToManyField('Person', through="Person2Alert", blank=True)
    target_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'alert'
