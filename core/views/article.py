from django_restql.mixins import QueryArgumentsMixin

from core.filters import ArticleFilterSet
from core.models import Article
from core.serializers import ArticleSerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class ArticleViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilterSet
