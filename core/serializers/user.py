from rest_framework import serializers
from django_restql.fields import NestedField
from django_restql.mixins import DynamicFieldsMixin
from core.models import User


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwards = {'password': {'write_only': True}}

    def save(self, **kwargs):
        account = User(email=self.validated_data['email'],
                       username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        account.set_password(password)
        account.save()
        return account
