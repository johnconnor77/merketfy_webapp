from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer
from rest_framework import serializers

from core.models import Article

from core.serializers import CompanySerializer, AlertSerializer, FavouriteSerializer, ImageSerializer


class ArticleSerializer(DynamicFieldsMixin, NestedModelSerializer):
    company = NestedField(CompanySerializer, accept_pk_only=True)
    price = serializers.FloatField(min_value=0.0)
    alerts = NestedField(AlertSerializer, required=False, many=True)
    favourites = NestedField(FavouriteSerializer, required=False, many=True)
    images = NestedField(ImageSerializer, required=False, many=True)

    class Meta:
        model = Article
        fields = '__all__'
