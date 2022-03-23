from django_filters import DateFromToRangeFilter

from core.filters import BaseFilterSet
from core.filters.constants import ID_LOOKUP_EXPR, STRING_LOOKUP_EXPR, QTY_LOOKUP_EXPR
from core.models import Article


class ArticleFilterSet(BaseFilterSet):
    class Meta:
        model = Article
        fields = {
            'company': ID_LOOKUP_EXPR,
            'article_category': ID_LOOKUP_EXPR,
            'article_type': ID_LOOKUP_EXPR,
            'name': STRING_LOOKUP_EXPR,
            'price': QTY_LOOKUP_EXPR,
            'shipping_price': QTY_LOOKUP_EXPR,
            'rating': QTY_LOOKUP_EXPR
        }
