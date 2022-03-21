from django.db import models

from core.models.constants import ENUM_SHORT_NAME_LENGTH, ENUM_NAME_LENGTH


class ModelBaseWithTimeStamps(models.Model):
    """
    Abstract base class for a model to add created_at and updated_at fields.
    You can not assign these attributes directly, they are managed by Django
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MerketfyBase(ModelBaseWithTimeStamps):
    class Meta:
        abstract = True


class ModelBaseWithNames(models.Model):
    short_name = models.CharField(
        max_length=ENUM_SHORT_NAME_LENGTH,
        unique=True,
        help_text="Short name. Unique identifier of the enumerate.",
    )
    name = models.CharField(max_length=ENUM_NAME_LENGTH, unique=True)


class MerketfyEnumBase(MerketfyBase, ModelBaseWithNames):
    class Meta:
        abstract = True


class EnumModelBase(MerketfyEnumBase):
    def __str__(self):
        """A simple string representation of the model."""
        return self.name
