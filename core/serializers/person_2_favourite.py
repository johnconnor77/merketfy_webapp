from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import Person2Favourite


class Person2FavouriteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Person2Favourite
        exclude = '__all__'
