from rest_framework import serializers


class AuthCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
