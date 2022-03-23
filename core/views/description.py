from rest_framework import filters, mixins, pagination, status, viewsets

# from core.filters import DescriptionFilterSet
from core.models import Description
from core.serializers import DescriptionSerializer


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    # filterset_class = DescriptionFilterSet
