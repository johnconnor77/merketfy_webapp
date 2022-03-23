from rest_framework import filters, mixins, pagination, status, viewsets

# from core.filters import EnumCompanyTypeFilterSet
from core.models import EnumCompanyType
from core.serializers import EnumCompanyTypeSerializer


class EnumCompanyTypeViewSet(viewsets.ModelViewSet):
    queryset = EnumCompanyType.objects.all()
    serializer_class = EnumCompanyTypeSerializer
    # filterset_class = EnumCompanyTypeFilterSet
