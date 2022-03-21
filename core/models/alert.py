from django.db import models

from core.models import User, Article
from core.models.base_classes import MerketfyBase


class Alert(MerketfyBase):
    article = models.ForeignKey(
        Article,
        on_delete=models.PROTECT)

    users = models.ManyToManyField(
        User,
        related_name="alerts")

    low_limit = models.FloatField()

