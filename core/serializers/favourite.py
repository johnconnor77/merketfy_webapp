from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer

from core.models import Alert


class FavouriteSerializer(DynamicFieldsMixin, NestedModelSerializer):

    class Meta:
        model = Alert
        fields = '__all__'
