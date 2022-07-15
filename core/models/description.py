from django.db import models
from django.db.models import JSONField

from core.models.base_classes import MerketfyBase


class Description(MerketfyBase):
    article = models.ForeignKey(
        'Article',
        on_delete=models.PROTECT,
        related_name="companies")
    description = models.CharField(max_length=1024)
    attributes = JSONField(blank=True, default=dict)

    class Meta:
        managed = True
        db_table = 'description'
