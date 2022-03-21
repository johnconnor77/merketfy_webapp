from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters import EnumArticleTypeFilterSet
from core.models import EnumArticleType
from core.serializers import EnumArticleTypeSerializer


class EnumArticleTypeViewSet(viewsets.ModelViewSet):
    queryset = EnumArticleType.objects.all()
    serializer_class = EnumArticleTypeSerializer
    filterset_class = EnumArticleTypeFilterSet
