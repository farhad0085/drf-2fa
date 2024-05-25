from django.dispatch import receiver, Signal
from drf_2fa.backends import BaseOTPBackend
from drf_2fa.settings import drf_2fa_settings


otp_required_signal = Signal(["user"])


@receiver(otp_required_signal)
def handle_otp_required_signal(user, *args, **kwargs):
    # create otp in database using backend class
    backend: BaseOTPBackend = drf_2fa_settings.DEFAULT_OTP_BACKEND()
    backend.save_and_send_otp_code(user)
