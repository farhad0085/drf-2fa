from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from drf_2fa.settings import drf_2fa_settings


User = get_user_model()


class AuthSecret(models.Model):
    """
    We might use this model for third party authenticator apps
    such as Google Authenticator
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    secret = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_auth_secret(self):
        pass


class OTPCode(models.Model):
    """
    Store otp code for the backends which sends otp to user
    such as EmailOTPBackend, SMSOTPBackend
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    otp_code = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def is_expired(cls, otp_obj):
        """Check if OTP is expired or not"""

        otp_expire = drf_2fa_settings.OTP_EXPIRE
        if otp_expire is None:
            return False
        expiration_time = otp_obj.created_at + otp_expire
        return timezone.now() > expiration_time

    @classmethod
    def is_valid(cls, user, otp_code):
        # check if otp is valid, and not expired
        otp_obj = cls.objects.filter(user=user, otp_code=otp_code).first()

        if not otp_obj:
            return False
        
        return not cls.is_expired(otp_obj), otp_obj
