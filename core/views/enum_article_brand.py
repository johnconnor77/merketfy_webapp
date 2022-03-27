from rest_framework import filters, mixins, pagination, status, viewsets

# from core.filters import EnumArticleCategoryFilterSet
from core.models import EnumArticleBrand
from core.serializers import EnumArticleBrandSerializer


class EnumArticleBrandViewSet(viewsets.ModelViewSet):
    queryset = EnumArticleBrand.objects.all()
    serializer_class = EnumArticleBrandSerializer
    # filterset_class = EnumArticleCategoryFilterSet
