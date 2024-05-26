from django.urls import path
from .views import GetAuthSecretAPIView, VerifyOTPAPIView


urlpatterns = [
    path('verify-otp/', VerifyOTPAPIView.as_view()),
    path('get-auth-secret/', GetAuthSecretAPIView.as_view()),
]
