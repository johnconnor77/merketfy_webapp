from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import EnumArticleBrand


class EnumArticleBrandSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = EnumArticleBrand
        exclude = ('created_at', 'updated_at')
