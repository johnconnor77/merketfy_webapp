from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer

from core.models import Company

from core.serializers import EnumCompanyTypeSerializer


class CompanySerializer(DynamicFieldsMixin, NestedModelSerializer):
    company_type = NestedField(EnumCompanyTypeSerializer, accept_pk_only=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
