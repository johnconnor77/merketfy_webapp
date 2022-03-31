from django_restql.mixins import QueryArgumentsMixin

# from core.filters import EnumArticleCategoryFilterSet
from core.models import EnumArticleBrand
from core.serializers import EnumArticleBrandSerializer
from core.views.base_classes import MerketfyReadOnlyViewSetBase


class EnumArticleBrandViewSet(QueryArgumentsMixin, MerketfyReadOnlyViewSetBase):
    queryset = EnumArticleBrand.objects.all()
    serializer_class = EnumArticleBrandSerializer
    # filterset_class = EnumArticleCategoryFilterSet
