from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from user.serializers import *
from user.models import *


class LoginView(APIView):
    """Class based view loggin in user and returning Auth Token."""

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        serializer_obj = LoginSerializer(data=data)

        serializer_obj.is_valid(raise_exception=True)
        username = serializer_obj.data["username"]
        password = serializer_obj.data["password"]

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Invalid Credentials"}, status=401)

        if not user.is_active:
            return Response(
                {"error": "Your account is inactive. Please contact support!"},
                status=401,
            )

        is_2fa_required = True
        
        if is_2fa_required:
            return Response({"message": "2FA authentication is required", "code": "2FA_REQUIRED"}, status=401)
        else:
            # Generate a auth code and send it to the user
            token, _ = Token.objects.get_or_create(user=user)
            response_data = UserAccountSerializer(user, context={"request": request}).data
            response_data["key"] = token.key
            return Response(response_data, status=200)


class UserInfo(APIView):
    """Check the userinfo of a user"""

    def get(self, request):
        user = request.user
        serializer = UserAccountSerializer(user, context={"request": request})
        return Response(serializer.data)
