from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.models import User2Favourite


class User2FavouriteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User2Favourite
        exclude = '__all__'
