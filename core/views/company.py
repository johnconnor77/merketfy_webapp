from django_restql.mixins import QueryArgumentsMixin


# from core.filters import CompanyFilterSet
from core.models import Company
from core.serializers import CompanySerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class CompanyViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # filterset_class = CompanyFilterSet
