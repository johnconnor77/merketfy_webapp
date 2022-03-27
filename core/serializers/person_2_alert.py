from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import Person2Alert


class Person2AlertSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Person2Alert
        exclude = '__all__'
