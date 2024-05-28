from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_2fa.models import AuthSecret
from drf_2fa.serializers import LoginSerializer, OTPCodeVerificationSerializer
from drf_2fa.settings import drf_2fa_settings
from drf_2fa.signals import otp_required_signal
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from rest_framework.permissions import IsAuthenticated


UserModel = get_user_model()

class VerifyOTPAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        otp_backend = drf_2fa_settings.OTP_BACKEND()

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


class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def get_serializer(self):
        return self.serializer_class

    def get_is_2fa_required(self, user):
        return True

    def post(self, request, format=None):
        data = request.data
        serializer = self.get_serializer()(data=data)

        serializer.is_valid(raise_exception=True)
        username = serializer.data["username"]
        password = serializer.data["password"]

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Invalid Credentials"}, status=401)

        if not user.is_active:
            return Response(
                {"error": "Your account is inactive. Please contact support!"},
                status=401,
            )

        is_2fa_required = self.get_is_2fa_required(user)
        if is_2fa_required:
            otp_required_signal.send(sender=request, user=user)
            return Response({
                "message": "2FA authentication is required",
                "user_id": user.id,
                "is_2fa_required": is_2fa_required
            })
        else:
            # Generate a auth code and send it to the user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message": "Login Successfully!", "api_token": token.key})
