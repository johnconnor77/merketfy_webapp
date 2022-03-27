from rest_framework import filters, mixins, pagination, status, viewsets

# from core.filters import DescriptionFilterSet
from core.models import Image
from core.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # filterset_class = DescriptionFilterSet
