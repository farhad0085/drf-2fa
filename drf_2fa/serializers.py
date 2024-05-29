from rest_framework import serializers


class OTPCodeVerificationSerializer(serializers.Serializer):
    """
    Serializer for validating OTP code verification requests.

    This serializer defines the structure and validation rules for requests
    to verify OTP codes. It includes fields for the user ID and the OTP code.
    """
    user_id = serializers.CharField()
    otp_code = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    """
    Serializer for validating login requests.

    This serializer defines the structure and validation rules for login requests.
    It includes fields for the username and password.
    """
    username = serializers.CharField()
    password = serializers.CharField()

