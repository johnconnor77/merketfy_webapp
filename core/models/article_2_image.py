from django.db import models

from .base_classes import MerketfyBase


class Article2Image(MerketfyBase):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, db_column='article_id')
    image = models.ForeignKey('Image', on_delete=models.CASCADE, db_column='image_id')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'article_2_image'
        unique_together = (('article', 'image'),)
