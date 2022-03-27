from django.db import models

from core.models.base_classes import MerketfyBase


class Alert(MerketfyBase):
    article = models.ForeignKey(
        'Article',
        on_delete=models.PROTECT)
    users = models.ManyToManyField('User', through="User2Alert", blank=True)
    target_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'alert'
