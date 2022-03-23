from rest_framework import filters, mixins, pagination, status, viewsets

# from core.filters import EnumArticleCategoryFilterSet
from core.models import EnumArticleCategory
from core.serializers import EnumArticleCategorySerializer


class EnumArticleCategoryViewSet(viewsets.ModelViewSet):
    queryset = EnumArticleCategory.objects.all()
    serializer_class = EnumArticleCategorySerializer
    # filterset_class = EnumArticleCategoryFilterSet
