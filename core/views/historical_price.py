from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters import HistoricalPriceFilterSet
from core.models import HistoricalPrice
from core.serializers import HistoricalPriceSerializer


class HistoricalPriceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPrice.objects.all()
    serializer_class = HistoricalPriceSerializer
    filterset_class = HistoricalPriceFilterSet
