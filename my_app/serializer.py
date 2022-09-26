from rest_framework import serializers
from .models import User, Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["account_password"]
