from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer
from rest_framework import serializers

from core.models import HistoricalPrice
from core.serializers import ArticleSerializer


class HistoricalPriceSerializer(DynamicFieldsMixin, NestedModelSerializer):
    article = NestedField(ArticleSerializer, read_only=True, accept_pk_only=True)
    price = serializers.FloatField(min_value=0.0)

    class Meta:
        model = HistoricalPrice
        fields = '__all__'
