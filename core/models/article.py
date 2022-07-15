from django.db import models

from core.models.base_classes import MerketfyBase
from core.models.model_utils.article_choices_field import ArticleCategoryChoices, ArticleTypeChoices, ArticleBrandChoices


class Article(MerketfyBase):
    company = models.ForeignKey(
        'Company',
        on_delete=models.PROTECT,
        related_name="articles")
    article_category: ArticleCategoryChoices = models.CharField(
        choices=ArticleCategoryChoices.ARTICLE_CATEGORY_CHOICES,
        max_length=100,
        default=ArticleCategoryChoices.UNKNOWN
    )
    article_type: ArticleTypeChoices = models.CharField(
        choices=ArticleTypeChoices.ARTICLE_TYPE_CHOICES,
        max_length=100,
        default=ArticleTypeChoices.UNKNOWN
    )
    article_brand: ArticleBrandChoices = models.CharField(
        choices=ArticleBrandChoices.ARTICLE_BRAND_CHOICES,
        max_length=100,
        default=ArticleBrandChoices.UNKNOWN
    )
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(max_length=200)
    price = models.FloatField()
    shipping_price = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    images = models.ManyToManyField('Image', through="Article2Image", blank=True)

    class Meta:
        managed = True
        db_table = 'article'
