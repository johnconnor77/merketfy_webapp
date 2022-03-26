from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer
from rest_framework import serializers

from core.models import Article

from core.serializers import CompanySerializer, EnumArticleCategorySerializer, EnumArticleBrandSerializer, \
    EnumArticleTypeSerializer, AlertSerializer, FavouriteSerializer


class ArticleSerializer(DynamicFieldsMixin, NestedModelSerializer):
    company = NestedField(CompanySerializer, accept_pk_only=True)
    article_category = NestedField(EnumArticleCategorySerializer, accept_pk_only=True, read_only=True)
    article_type = NestedField(EnumArticleTypeSerializer, accept_pk_only=True, read_only=True)
    article_brand = NestedField(EnumArticleBrandSerializer, accept_pk_only=True, read_only=True)
    price = serializers.FloatField(min_value=0.0)
    alerts = NestedField(AlertSerializer, required=False, many=True)
    favourites = NestedField(FavouriteSerializer, required=False, many=True)

    class Meta:
        model = Article
        fields = '__all__'
