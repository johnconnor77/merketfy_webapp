from django_restql.mixins import QueryArgumentsMixin

# from core.filters import DescriptionFilterSet
from core.models import Description
from core.serializers import DescriptionSerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class DescriptionViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    # filterset_class = DescriptionFilterSet
