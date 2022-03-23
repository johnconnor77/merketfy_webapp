from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer

from core.models import Description


class DescriptionSerializer(DynamicFieldsMixin, NestedModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'
