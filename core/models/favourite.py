from django.db import models

from core.models.base_classes import MerketfyBase


class Favourite(MerketfyBase):
    article = models.ForeignKey(
        'Article',
        on_delete=models.PROTECT)
    persons = models.ManyToManyField('Person', through="Person2Favourite", blank=True)

    class Meta:
        managed = False
        db_table = 'favourite'
