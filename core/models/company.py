from django.db import models

from core.models.base_classes import MerketfyBase
from core.models.model_utils.company_choices_field import CompanyTypeChoices


class Company(MerketfyBase):
    name = models.CharField(max_length=128)
    company_type: CompanyTypeChoices = models.CharField(
        choices=CompanyTypeChoices.COMPANY_TYPE_CHOICES,
        max_length=100,
        default=CompanyTypeChoices.UNKNOWN
    )
    note = models.TextField()
    icon_url = models.URLField(max_length=200)

    class Meta:
        managed = False
        db_table = 'company'
