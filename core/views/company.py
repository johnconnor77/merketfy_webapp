from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters import CompanyFilterSet
from core.models import Company
from core.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilterSet
