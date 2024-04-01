from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import *

UserModel: UserAccount = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        exclude = ["user_permissions", "groups"]
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def validate_email(self, email):
        if UserAccount.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email
