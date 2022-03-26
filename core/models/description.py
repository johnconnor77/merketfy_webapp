from django.db import models
from django.contrib.postgres.fields import JSONField

from core.models.base_classes import MerketfyBase


class Description(MerketfyBase):
    article = models.ForeignKey(
        'Article',
        on_delete=models.PROTECT,
        related_name="companies")
    description = models.CharField(max_length=1024)
    attributes = JSONField(blank=True, default=dict)
