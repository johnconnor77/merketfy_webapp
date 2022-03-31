from django_restql.mixins import QueryArgumentsMixin

# from core.filters import EnumArticleCategoryFilterSet
from core.models import EnumArticleCategory
from core.serializers import EnumArticleCategorySerializer
from core.views.base_classes import MerketfyReadOnlyViewSetBase


class EnumArticleCategoryViewSet(QueryArgumentsMixin, MerketfyReadOnlyViewSetBase):
    queryset = EnumArticleCategory.objects.all()
    serializer_class = EnumArticleCategorySerializer
    # filterset_class = EnumArticleCategoryFilterSet
