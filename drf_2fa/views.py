from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_2fa.serializers import OTPCodeVerificationSerializer
from drf_2fa.settings import drf_2fa_settings
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class VerifyOTPAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        otp_backend = drf_2fa_settings.DEFAULT_OTP_BACKEND()

        serializer = OTPCodeVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data["otp_code"]
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Invalid Credentials"}, status=401)
        
        if not user.is_active:
            return Response(
                {"error": "Your account is inactive. Please contact support!"},
                status=401,
            )

        verified = otp_backend.verify_otp(user, otp_code)
        if verified:
            # Generate a auth code and send it to the user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "OTP Verified Successfully!",
                "status": "SUCCESS",
                "api_token": token.key
            })
        return Response({"message": "Invalid or expired OTP provided!", "status": "FAILURE"}, 400)
