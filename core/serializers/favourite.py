from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer

from core.models import Alert
from core.serializers import UserSerializer


class FavouriteSerializer(DynamicFieldsMixin, NestedModelSerializer):
    users = NestedField(UserSerializer, many=True, required=False)

    class Meta:
        model = Alert
        fields = '__all__'
