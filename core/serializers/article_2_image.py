from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import Article2Image


class Article2ImageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Article2Image
        exclude = '__all__'
