from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import EnumCompanyType


class EnumArticleTypeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = EnumCompanyType
        exclude = ('created_at', 'updated_at')
