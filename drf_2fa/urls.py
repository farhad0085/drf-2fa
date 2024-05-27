from django.urls import path
from .views import GetAuthSecretAPIView, LoginAPIView, VerifyOTPAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login_url"),
    path('verify-otp/', VerifyOTPAPIView.as_view()),
    path('get-auth-secret/', GetAuthSecretAPIView.as_view()),
]
