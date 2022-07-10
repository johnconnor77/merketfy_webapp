import datetime

from django.db import models

from core.models.constants import ENUM_SHORT_NAME_LENGTH, ENUM_NAME_LENGTH


class MerketfyBase(models.Model):
    """
    Abstract base class for a model to add created_at and updated_at fields.
    You can not assign these attributes directly, they are managed by Django
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
