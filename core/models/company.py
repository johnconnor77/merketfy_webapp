from django.db import models

from core.models.base_classes import MerketfyBase


class Company(MerketfyBase):
    name = models.CharField(max_length=128)
    company_type = models.ForeignKey(
        'EnumCompanyType',
        on_delete=models.PROTECT,
        db_column="company_type",
        to_field='short_name',
        related_name="companies"
    )
    note = models.TextField()
    icon_url = models.URLField(max_length=200)
