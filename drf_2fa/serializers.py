from rest_framework import serializers


class OTPCodeVerificationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    otp_code = serializers.CharField()
