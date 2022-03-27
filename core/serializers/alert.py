from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer
from rest_framework import serializers

from core.models import Alert
from core.serializers.person import PersonSerializer


class AlertSerializer(DynamicFieldsMixin, NestedModelSerializer):
    persons = NestedField(PersonSerializer, many=True, required=False)
    target_price = serializers.FloatField(min_value=0.0)

    class Meta:
        model = Alert
        fields = '__all__'
