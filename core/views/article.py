from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters import ArticleFilterSet
from core.models import Article
from core.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilterSet
