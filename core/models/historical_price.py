from django.db import models

from core.models import EnumCompanyType, Article
from core.models.base_classes import MerketfyBase


class HistoricalPrice(MerketfyBase):
    article = models.ForeignKey(
        Article,
        on_delete=models.PROTECT)
    price = models.FloatField()
