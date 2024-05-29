from django.dispatch import receiver, Signal
from drf_2fa.backends import BaseOTPBackend
from drf_2fa.settings import drf_2fa_settings


otp_required_signal = Signal(["user"])


@receiver(otp_required_signal)
def handle_otp_required_signal(user, *args, **kwargs):
    """
    Receiver function to handle the `otp_required_signal`

    This function is called when the `otp_required_signal` signal is emitted,
    indicating that an OTP is required for the specified user.

    Note:
        This function retrieves the OTP backend specified in the DRF 2FA settings,
        creates an instance of the backend, and then saves and sends the OTP code
        to the user.
    """
    backend: BaseOTPBackend = drf_2fa_settings.OTP_BACKEND()
    backend.save_and_send_otp_code(user)
