from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer

from core.models import Image


class ImageSerializer(DynamicFieldsMixin, NestedModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
