from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_2fa.settings import drf_2fa_settings


class VerifyOTPAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        otp_backend = drf_2fa_settings.DEFAULT_OTP_BACKEND
        print(request.data)
        otp = request.data.get("otp_key")

        verified = otp_backend().verify_otp(request.user, otp)
        if verified:
            return Response({"message": "OTP Verified Successfully!", "status": "SUCCESS"}, 200)
        return Response({"message": "Invalid or expired OTP provided!", "status": "FAILURE"}, 400)
