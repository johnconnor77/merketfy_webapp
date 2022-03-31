from django_restql.mixins import QueryArgumentsMixin

# from core.filters import DescriptionFilterSet
from core.models import Image
from core.serializers import ImageSerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class ImageViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # filterset_class = DescriptionFilterSet
