from rest_framework import filters, mixins, pagination, status, viewsets

from core.filters import UserFilterSet
from core.models import User
from core.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilterSet
