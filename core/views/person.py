from django_restql.mixins import QueryArgumentsMixin

# from core.filters import UserFilterSet
from core.models import Person
from core.serializers import PersonSerializer
from core.views.base_classes import MerketfyReadWriteViewSetBase


class PersonViewSet(QueryArgumentsMixin, MerketfyReadWriteViewSetBase):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # filterset_class = UserFilterSet
