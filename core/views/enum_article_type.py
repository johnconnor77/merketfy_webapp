from django_restql.mixins import QueryArgumentsMixin

# from core.filters import EnumArticleTypeFilterSet
from core.models import EnumArticleType
from core.serializers import EnumArticleTypeSerializer
from core.views.base_classes import MerketfyReadOnlyViewSetBase


class EnumArticleTypeViewSet(QueryArgumentsMixin, MerketfyReadOnlyViewSetBase):
    queryset = EnumArticleType.objects.all()
    serializer_class = EnumArticleTypeSerializer
    # filterset_class = EnumArticleTypeFilterSet
