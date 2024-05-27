from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import *


class UserInfo(APIView):
    """Check the userinfo of a user"""

    def get(self, request):
        user = request.user
        serializer = UserAccountSerializer(user, context={"request": request})
        return Response(serializer.data)
