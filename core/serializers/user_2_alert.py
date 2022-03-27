from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import User2Alert


class User2AlertSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User2Alert
        exclude = '__all__'
