from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_2fa.serializers import OTPCodeVerificationSerializer
from drf_2fa.settings import drf_2fa_settings
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class VerifyOTPAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        otp_backend = drf_2fa_settings.DEFAULT_OTP_BACKEND()

        serializer = OTPCodeVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data["otp_code"]
        user_id = serializer.validated_data["user_id"]
        user = UserModel.objects.filter(id=user_id).first()

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
