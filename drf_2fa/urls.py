from django.urls import path
from .views import VerifyOTPAPIView


urlpatterns = [
    path('verify-otp/', VerifyOTPAPIView.as_view()),
]
