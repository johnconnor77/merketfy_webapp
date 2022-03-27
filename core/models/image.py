from django.db import models
from django.contrib.postgres.fields import JSONField

from core.models.base_classes import MerketfyBase


class Image(MerketfyBase):
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=200)
    articles = models.ManyToManyField('Article', through="Article2Image", blank=True)

    class Meta:
        managed = False
        db_table = 'image'
