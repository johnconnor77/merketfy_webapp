from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer

from core.models import Company


class CompanySerializer(DynamicFieldsMixin, NestedModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
