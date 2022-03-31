# from core.filters import AlertFilterSet
from django_restql.mixins import QueryArgumentsMixin

from core.models import Alert
from core.serializers import AlertSerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class AlertViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    # filterset_class = AlertFilterSet
