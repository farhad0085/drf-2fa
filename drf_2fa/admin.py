from django.contrib import admin
from .models import OTPCode

class OTPCodeAdmin(admin.ModelAdmin):
    list_display = ["user", "otp_code", "created_at"]

admin.site.register(OTPCode, OTPCodeAdmin)
