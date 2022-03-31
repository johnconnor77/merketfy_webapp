from django_restql.mixins import QueryArgumentsMixin

# from core.filters import EnumCompanyTypeFilterSet
from core.models import EnumCompanyType
from core.serializers import EnumCompanyTypeSerializer
from core.views.base_classes import MerketfyReadOnlyViewSetBase


class EnumCompanyTypeViewSet(QueryArgumentsMixin, MerketfyReadOnlyViewSetBase):
    queryset = EnumCompanyType.objects.all()
    serializer_class = EnumCompanyTypeSerializer
    # filterset_class = EnumCompanyTypeFilterSet
