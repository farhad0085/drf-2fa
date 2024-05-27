from rest_framework import serializers


class OTPCodeVerificationSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    otp_code = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

