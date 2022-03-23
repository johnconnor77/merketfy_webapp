from django.db import models

from core.models import Company, EnumArticleCategory, EnumArticleType, EnumArticleBrand
from core.models.base_classes import MerketfyBase


class Article(MerketfyBase):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name="articles")
    article_category = models.ForeignKey(
        EnumArticleCategory,
        on_delete=models.PROTECT,
        related_name="articles")
    article_type = models.ForeignKey(
        EnumArticleType,
        on_delete=models.PROTECT,
        related_name="articles")
    brand = models.ForeignKey(
        EnumArticleBrand,
        on_delete=models.PROTECT,
        related_name="articles")
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=200)
    price = models.FloatField()
    shipping_price = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
