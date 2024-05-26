from django.contrib import admin
from .models import OTPCode
from drf_2fa.settings import drf_2fa_settings


class OTPCodeAdmin(admin.ModelAdmin):
    list_display = ["user", "otp_code", "created_at"]


if drf_2fa_settings.SHOW_OTP_MODEL_ADMIN:
    admin.site.register(OTPCode, OTPCodeAdmin)
