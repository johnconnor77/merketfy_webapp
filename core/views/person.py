from rest_framework import filters, mixins, pagination, status, viewsets

# from core.filters import UserFilterSet
from core.models import Person
from core.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # filterset_class = UserFilterSet
