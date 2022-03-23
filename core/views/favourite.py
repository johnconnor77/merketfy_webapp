from rest_framework import filters, mixins, pagination, status, viewsets

# from core.filters import FavouriteFilterSet
from core.models import Favourite
from core.serializers import FavouriteSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    # filterset_class = FavouriteFilterSet
