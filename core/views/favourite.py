from django_restql.mixins import QueryArgumentsMixin

# from core.filters import FavouriteFilterSet
from core.models import Favourite
from core.serializers import FavouriteSerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class FavouriteViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    # filterset_class = FavouriteFilterSet
