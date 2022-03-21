from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters import AlertFilterSet
from core.models import Alert
from core.serializers import AlertSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filterset_class = AlertFilterSet
