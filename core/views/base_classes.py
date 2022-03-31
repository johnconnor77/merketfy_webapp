import django_filters
from rest_framework import filters, mixins, pagination, status, viewsets


class MerketfyViewSetMixin:
    """
    Mixin for common view sets that sit outside the base hierarchy.
    """

    # Override this list if required. For example to allow put method
    # Restrict viewsets to allow only this methods.
    http_method_names = ['get', 'post', 'patch', 'head', 'options', 'trace']

    # Set django-filters as the last filter backend for our views. This way we can guarantee
    # that our custom filterset classes are the last ones to be applied when filtering or sorting
    # our querysets.
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class MerketfyReadOnlyViewSetBase(MerketfyViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    Base class for read only views.  Place holder for common read code.
    """

    http_method_names = ['get', 'head', 'options', 'trace']


class MerketfyReadWriteViewSetBase(
    MerketfyViewSetMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.ReadOnlyModelViewSet,
):
    """
    Base class for read & write views.  Place holder for common write code.
    """

    # Allows POST to receive a list of objects to create
    # Set to False on child class to only allow creation of one object at a time
    handle_many = True
