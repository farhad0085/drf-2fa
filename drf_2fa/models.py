import qrcode
import qrcode.image.svg
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from drf_2fa.settings import drf_2fa_settings
from urllib.parse import quote
import base64
import secrets


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
        secret_bytes = secrets.token_bytes(20)  # 20 bytes to match 160 bits
        secret_base32 = base64.b32encode(secret_bytes).decode('utf-8')
        return secret_base32[:32]

    def generate_qr_code(self, name=None):
        issuer_name = drf_2fa_settings.QR_ISSUER_NAME
        name = self.user.email
        qr_uri = f"otpauth://totp/{quote(issuer_name)}:{quote(name)}?secret={self.secret}&issuer={quote(issuer_name)}"

        image_factory = qrcode.image.svg.SvgPathImage
        qr_code_image = qrcode.make(qr_uri, image_factory=image_factory)
        
        # The result is going to be an HTML <svg> tag
        return qr_code_image.to_string().decode('utf_8')


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
        otp_obj = cls.objects.filter(user=user, otp_code=otp_code).order_by('-created_at').first()

        if not otp_obj:
            return False, None
        
        return not cls.is_expired(otp_obj), otp_obj
