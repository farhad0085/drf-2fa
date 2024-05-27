from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_2fa.models import AuthSecret
from drf_2fa.serializers import OTPCodeVerificationSerializer
from drf_2fa.settings import drf_2fa_settings
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


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


class GetAuthSecretAPIView(APIView):
    """Get auth secret for authenticator app"""
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        obj, created = AuthSecret.objects.get_or_create(user=request.user)
        if created:
            auth_secret = obj.generate_auth_secret()
            obj.secret = auth_secret
            obj.save()

        return Response({
            "name": request.user.email,
            "issuer_name": drf_2fa_settings.QR_ISSUER_NAME,
            "auth_secret": obj.secret,
            "qr_code": obj.generate_qr_code()
        })

