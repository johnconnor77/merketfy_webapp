from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import EnumArticleCategory


class EnumArticleCategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = EnumArticleCategory
        exclude = ('created_at', 'updated_at')
