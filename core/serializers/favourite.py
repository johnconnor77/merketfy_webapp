from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer

from core.models import Alert
from core.serializers import PersonSerializer


class FavouriteSerializer(DynamicFieldsMixin, NestedModelSerializer):
    persons = NestedField(PersonSerializer, many=True, required=False)

    class Meta:
        model = Alert
        fields = '__all__'
