from django_restql.mixins import QueryArgumentsMixin

# from core.filters import HistoricalPriceFilterSet
from core.models import HistoricalPrice
from core.serializers import HistoricalPriceSerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class HistoricalPriceViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = HistoricalPrice.objects.all()
    serializer_class = HistoricalPriceSerializer
    # filterset_class = HistoricalPriceFilterSet
